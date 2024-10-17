import time
import subprocess

def print_statements(statements, interval):
    for i, statement in enumerate(statements):
        print(f"Chief: {statement}")
        time.sleep(interval)
    
        # Switch to JavaScript after certain Python statements
        if i == 4:  # After 3rd and 4th Python statements
            run_javascript(0, interval)
            run_javascript(1, interval)

def run_javascript(statement_index, interval):
    try:
        # Pass the current statement index to the JavaScript script
        subprocess.run(["node", "./js_scripts/misheveve.js", str(statement_index), str(interval)])
    except Exception as e:
        print(f"Error running JavaScript: {e}")

if __name__ == "__main__":
    statements = [
        "Mama unapika mboga gani", 
        "Leo nimeunda Misheveve",
        "Sikutaka hizi, nilitaka sarati",
        "Akaanza kum...zaba mama makofi",
        "Makofi mingi tena saidi",
        "Alianza kwa kumtafuna mzee vidole",
        "Anatafuna mzee vidole ni kama anatafuna omena",
        "Na kumbe anafanya hesabu ya minus kwa uhai ya mzee",
        "Na mzee ni mkasa",
    ]
    interval = 1.5  # 2-second interval
    print_statements(statements, interval)
