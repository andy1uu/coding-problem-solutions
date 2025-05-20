function isValid(s: string): boolean {
    let brackets: string[] = [];

    if (s.length === 1) {
        return false
    }

    for (const bracket of s) {
        if (bracket === "]" && brackets.length > 0 && brackets[brackets.length - 1] === "[") {
            brackets.pop();
        }
        else if (bracket === "}" && brackets.length > 0 && brackets[brackets.length - 1] === "{") {
            brackets.pop();
        }
        else if (bracket === ")" && brackets.length > 0 && brackets[brackets.length - 1] === "(") {
            brackets.pop();
        }
        else if(bracket === "[" || bracket === "{" || bracket === "(") {
            brackets.push(bracket)
        }
        else {
            return false
        }
    }
    
    return brackets.length === 0
};