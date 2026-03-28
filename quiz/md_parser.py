"""
Markdown quiz file parser.
Parses .md files with quiz questions in the specified format.
"""
import re
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension


def render_markdown(text):
    """Render markdown text to HTML with syntax highlighting."""
    if not text:
        return ''
    md = markdown.Markdown(
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(css_class='highlight', linenums=False, guess_lang=False),
            'tables',
        ]
    )
    return md.convert(text)


def render_inline_markdown(text):
    """Render markdown text to inline HTML (no wrapping <p> tags).

    Used for option text where backticks should become <code> and
    HTML-like content (e.g. <class 'int'>) must be escaped, but
    block-level <p> wrapping is unwanted.
    """
    if not text:
        return ''
    html = render_markdown(text)
    # Strip single wrapping <p>...</p> for inline display
    html = re.sub(r'^\s*<p>(.*)</p>\s*$', r'\1', html, flags=re.DOTALL)
    return html


def parse_quiz_markdown(content):
    """
    Parse a markdown quiz file and return a list of question dicts.

    Expected format:
    ## Savol N
    <question text, may include code blocks>
    - [A] option text
    - [B] option text
    - [C] option text
    - [D] option text (optional)
    > **To'g'ri javob:** X
    > **Tushuntirish:** explanation text
    ---
    """
    questions = []

    # Split by ## Savol headers
    blocks = re.split(r'(?=^## )', content, flags=re.MULTILINE)

    for block in blocks:
        block = block.strip()
        if not block.startswith('## '):
            continue

        # Remove trailing ---
        block = re.sub(r'\n---\s*$', '', block).strip()

        question = parse_question_block(block)
        if question:
            questions.append(question)

    return questions


def parse_question_block(block):
    """Parse a single question block."""
    lines = block.split('\n')

    # Extract question number from header
    header = lines[0]
    match = re.match(r'## Savol\s+(\d+)', header)
    if not match:
        return None
    order_index = int(match.group(1))

    # Remove header line
    rest = '\n'.join(lines[1:]).strip()

    # Extract correct answer from blockquote
    correct_option = ''
    correct_match = re.search(
        r'>\s*\*\*To\'g\'ri javob:\*\*\s*([A-Da-d])',
        rest
    )
    if correct_match:
        correct_option = correct_match.group(1).lower()

    # Extract explanation from blockquote
    explanation = ''
    expl_match = re.search(
        r'>\s*\*\*Tushuntirish:\*\*\s*(.*?)(?:\n(?!>)|$)',
        rest,
        re.DOTALL
    )
    if expl_match:
        explanation = expl_match.group(1).strip()

    # Remove blockquote lines (answer + explanation)
    rest_no_bq = re.sub(r'^>.*$', '', rest, flags=re.MULTILINE).strip()

    # Extract options: - [A] text, - [B] text, etc.
    options = {'a': '', 'b': '', 'c': '', 'd': ''}
    option_pattern = re.compile(r'^-\s*\[([A-Da-d])\]\s*(.*)', re.MULTILINE)
    for m in option_pattern.finditer(rest_no_bq):
        letter = m.group(1).lower()
        text = m.group(2).strip()
        options[letter] = text

    # Remove option lines to get question text
    question_text = option_pattern.sub('', rest_no_bq).strip()
    # Clean up extra blank lines
    question_text = re.sub(r'\n{3,}', '\n\n', question_text)

    if not question_text or not options.get('a'):
        return None

    return {
        'order_index': order_index,
        'question_md': question_text,
        'option_a': options['a'],
        'option_b': options['b'],
        'option_c': options['c'],
        'option_d': options['d'],
        'correct_option': correct_option,
        'explanation_md': explanation,
    }
