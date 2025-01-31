#!/bin/bash

# Definition of folders and files to create
FULL_SERVER_DIR="full_server"
CONTROLLERS_DIR="$FULL_SERVER_DIR/controllers"
ROUTES_DIR="$FULL_SERVER_DIR/routes"

# Creating folders
mkdir -p "$FULL_SERVER_DIR" "$CONTROLLERS_DIR" "$ROUTES_DIR"

# Creating main files
touch "0-console.js"
touch "1-stdin.js"
touch "2-read_file.js"
touch "3-read_file_async.js"
touch "4-http.js"
touch "5-http.js"
touch "6-http_express.js"
touch "7-http_express.js"

# Creating files for the structured server
touch "$FULL_SERVER_DIR/utils.js"
touch "$CONTROLLERS_DIR/AppController.js"
touch "$CONTROLLERS_DIR/StudentsController.js"
touch "$ROUTES_DIR/index.js"
touch "$FULL_SERVER_DIR/server.js"

# Adding configuration files
touch "package.json"
touch "babel.config.js"
touch ".eslintrc.js"
touch "README.md"
touch "database.csv"

# Confirmation message
echo "All project files and folders have been created."

# Running npm install to install dependencies
bun install

# Post-creation instructions
echo "Dependencies have been installed."
