const p_o = 'openParenthesis';
const p_c = 'closeParenthesis';
const s_o = 'openSquareBracket';
const s_c = 'closeSquareBracket';
const b_o = 'openBrace';
const b_c = 'closeBrace';

const getName = character => {
  switch (character) {
    case '(':
      return p_o;
    case ')':
      return p_c;
    case '[':
      return s_o;
    case ']':
      return s_c;
    case '{':
      return b_o;
    case '}':
      return b_c;
  }
};

const isOpen = character => {
  const openArray = ['(', '{', '['];
  return openArray.includes(character);
};

const isMatch = (c1, c2) => {
  return (
    (c1 === '{' && c2 === '}') ||
    (c1 === '[' && c2 === ']') ||
    (c1 === '(' && c2 === ')')
  );
};

const isValid = string => {
  const open = [];
  for (let i = 0; i < string.length; i++) {
    const c = string[i];
    if (isOpen(c)) {
      open.push(c);
    } else {
      if (open.length === 0) {
        return false;
      }
      if (!isMatch(open.pop(), c)) {
        return false;
      }
    }
  }

  if (open.length > 0) {
    return false;
  }

  return true;
};

console.log(isValid('({}[])'));
