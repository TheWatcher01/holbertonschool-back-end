/**
 * @file 1-stdin.js
 * @author TheWatcher01
 * @date 31-01-2025
 * @description Welcome message with input from STDIN
 */

process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('readable', () => {
  const name = process.stdin.read();

  if (name !== null) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
