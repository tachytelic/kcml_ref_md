# Program Resolution and Execution

> Before a KCML program runs, it goes through a resolution phase that validates structure, allocates variables, and sets up the data pointer — then execution begins at the first statement.

## Overview

Running a KCML program is a two-step process: **resolution** followed by **execution**. Resolution catches structural errors and allocates memory; only if resolution succeeds does execution begin.

## Starting Execution

A program can be started in several ways:

- Press **F11** (Execute) in the KCML Workbench.
- Enter `RUN` or `LOAD RUN` at the immediate mode prompt.
- Pass the program name as a command-line argument to the `kcml` utility from the OS shell:  
  `kcml -p myprog.kcml`

## The Resolution Phase

Before execution begins, KCML performs a resolution pass over the entire program:

1. **Syntax and structure check:** All line references, variable references, `FOR`/`NEXT` pairs, `REPEAT`/`UNTIL` pairs, `WHILE`/`WEND` pairs, `SELECT CASE` blocks, and `DO`/`ENDDO` groups are validated.

2. **Variable allocation:** `DIM` and `COM` statements are executed. Space is reserved for all variables not already defined. Numeric variables are initialized to zero; alpha variables are initialized to spaces.

3. **Data pointer initialization:** The `READ` statement's data pointer is set to the first item in the first `DATA` statement in the program.

If any error occurs during resolution, the process halts and an error is displayed. Execution does not begin.

**Resolution without execution** can be triggered with `RUN STOP` at the immediate mode prompt, or with **Shift-F9** in the Workbench. This is useful for checking syntax without running the program.

## Execution

Once resolution succeeds, execution begins at the first statement in the program and continues until one of the following occurs:

| Condition | Effect |
|-----------|--------|
| `STOP` statement | Halts execution and returns to Workbench/prompt |
| `$END` statement | Normal program termination |
| `END` statement | Normal program termination |
| `PANIC` statement | Abnormal termination |
| Last line reached | Program ends normally |
| Unhandled error | Execution stops with an error message |
| `TRAP` event | Control transferred to trap handler |

## Interrupting Execution

**HALT key:** Saves the current program state and switches to the Workbench debugger (or immediate mode prompt if the Workbench is unavailable). The program can be restarted from where it stopped with the `CONTINUE` command (or 'C' in the Workbench), provided no lines have been edited since the halt.

- To restart at a different line: use the 'S' command followed by 'C' in the Workbench, or `GOTO` then `CONTINUE` at the immediate mode prompt.
- **Single-stepping:** Pressing the **Spacebar** in the Workbench advances execution one line at a time.

**RESET key:** Terminates execution immediately (when enabled).

## After Editing

If any program lines are added, changed, or deleted after a halt, the program must be re-resolved before it can be restarted. Attempting to `CONTINUE` after editing without re-resolving will produce an error.

## Useful Debugging Commands

| Command / Key | Effect |
|---------------|--------|
| `CONTINUE` (`C`) | Restart after a HALT from the point of interruption |
| `CONTINUE NEXT` | Restart and stop just before the last `FOR`/`NEXT` loop completes its final iteration |
| `LIST RETURN` | Display the current contents of the return stack (active `FOR`/`NEXT` and `GOSUB` frames) |
| `RETURN CLEAR` | Clear the most recent return stack entry |
| `RETURN CLEAR ALL` | Clear the entire return stack |

## Notes

- Resolution executes `DIM` and `COM` statements — this means initialization expressions in those statements run at resolve time, not at the first line of the program body.
- The `$END` statement is the normal way to terminate a program in non-interactive (`-p`) mode.
- If a `TRAP` handler is active when an error occurs, the handler takes over rather than halting execution. See the `TRAP` reference for details.
- See also: `RUN`, `LOAD RUN`, `STOP`, `$END`, `CONTINUE`, `CONTINUE NEXT`, `LIST RETURN`, `RETURN CLEAR`, `TRAP`, `HALT`
