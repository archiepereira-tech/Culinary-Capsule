# Culinary-Capsule
A digital cookbook that sends individual recipes into the future via email.

## Usage
Simply visit https://archiepereira-tech.github.io/Culinary-Capsule/ to send a recipe. Click "Send Recipe" and fill out all necessary details. The email with the recipe will send on the date chosen. The recipient will recieve a recipe card from your "cookbook".

## Purpose
Families around the world have cookbooks passed down from generations, sharing unique recipes with strong cultural ties. Culinary Capsule is a stronger and safer digitized cookbook that allows users to share custom recipes to others, and into the future to emails of generations to come. It has a very simple UI and is designed for easy-of-use so users of all technical skill can share a piece of their culture with others. Users can send individual recipes that can be sent at anytime to any valid email inbox. Culinary Capsule provides a new innovative twist on reliable technologies to share recipes that unite people and maintain cultural values.

## Technical Details
Culinary Capsule utilizes multiple technologies for an efficient and fool-proof system. An HTML webpage hosted on GitHub Pages and developed with Bootstrap and JavaScript along with HTML will collect user recipes and sender/recipient information. All information is stored in a Postgres database using Supabase. Every morning (EST/CST), a GitHub Action runs a Python script (main.py), which uses various libraries (including SMTP) that collects all the day's recipes and sends them out as HTML emails via cookbook.culinarycapsule@gmail.com.
