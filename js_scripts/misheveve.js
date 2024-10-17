
function printStatements(statementIndex) {
    const statements = [
        "Baba bila shaka alifika kumuokoa mama",
        "Alimuangamiza vipi?",
    ];

    if (statementIndex < statements.length) {
        console.log(`Narrator: ${statements[statementIndex]}`);
        setTimeout(() => {}, interval * 1500); 
    } else {
        console.log("Invalid statement index");
    }
    
}
// Get the statement index passed from Python
const statementIndex = process.argv[2];  // Arguments passed from the Python subprocess
const interval = process.argv[3] || 1.5;   // Interval argument with a default value of 2 seconds

printStatements(statementIndex);