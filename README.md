# silverorange Python Developer Assessment Attempt

## Introduction

I understand the repos are to be anonymized, and I tried to stay true to that. However, there are following details about my setup/environment that I include that impacted my experience completing this exercise that I thought were important (or at least interesting!) to share. This theoretically shouldn't impact the anonymization, but I wanted to add this note anyways.

There may also be present/past tense inconsistencies, I'm also using this as my live notes page. For all I know you guys don't even look at this, but at least I have it for my own sake!

This is my first time working with Django, and although I have a Mac, I prefer working on my Windows machine and don't have a MacOS VM set up. After encountering this exercise I'll definitely set one up!

Since this is not going back upstream, I didn't add the original test repo as a git upstream to this fork, otherwise I would on a real project


## My process setting up
  My process running this exercise on a Windows environment in VS Code. I included these because from working, I've learned accurate repro steps are extremely important!

  My Windows setup process for replication (assuming already in desired directory with my fork pulled)
  1. Instead of 
  ```
  brew install uv
  ```
  I ran
  ```
  pip install uv
  ```

  2.
  ```
  uv sync
  ```
    > this creates a .venv
  ```
  .\.venv\Scripts\activate
  ```
  > In terminal it says "(silverorange-python-exercise)" rather than "(.venv)"
  ```
  uv run python manage.py migrate
  ```
  3. 
  ```
  pip install node
  ```
  4. 
  ```
  npm install
  ```
    4.1. Got a "1 high severity vulnerability"
      "To address all issues, run: 
      ```
      npm audit fix
      ```
  5. "make" doesn't natively run on Windows: I ran 
  ```
  choco install make
  ```
    After running, "make dev" works

    Verified with the included links on the README that the server was running


## Notes:
### Strange behaviour:
  Seemingly Django has a child process for running that can't be stopped on Windows reliably - I don't have a BREAK key on my keyboard, and running CTRL+C hangs the process. Even killing my terminal didn't seem to stop the server, as I would hard refresh my localhost:8000 and 8000/posts/ pages and they still showed. Only completely closing my VS Code seems to stop the server, giving me a 404 on the previous mentioned pages.

  However, this vastly slows my development having to close and reopen (folders, venvs, etc), so trying AI recommended steps I added the --noreload flag to the Makefile's runserver target > This still hangs, but it seems if I spam CTRL+C after "Y" eventually it silently dies?

  With the --noreload flag on, I added a line to welcome.html. On first soft refresh it showed, then no further changes showed. Strange

  Removed the --noreload flag, seems like the spam CTRL+C method may work even without it if I need to restart the server. Much better without the flag for the speed
  > Terming the program in terminal, refreshing the pages still shows the Django rather than 404
  > Maybe just Django behaviour?

### .gitignore
- My package-lock.json for my dependencies is not in the default gitignore, I'm deciding to not touch the gitignore and leave it default.

## Checklist
1. Create models for posts and authors in the blog app based on the data in JSON files.
> Done

2. Write an importer in Python that imports post and author data files from the data into the SQLite database configured in the Django project.
> Going to make in the main directory
> Wording doesn't say has to go through as a Django model, can I just load the JSONs directly to the SQLite DB?
> I'm going to store everything in the sqlite3 DB as text for now, then convert when retrieving
> Done

3. Update the post index view to load all published posts from the database in reverse chronological order.
- Update the template to render this list as HTML.
- Include the post titles and authors in the output.
- Make clicking a post go to the post details.

4. Add a post detail route to the blog app that will load a published post from the database from the id in the URL.
- The URL path should be of the form posts/[id].
> The post ids are stored as UUID in the DB, so I kept it as UUID
- The view and template should render the post content (title, body, author) as HTML.
- If the requested post is unavailable, show a 404 page.
- The post body is formatted as Markdown and the HTML should include the formatted Markdown.

5. Add basic CSS to the index and detail views. The SCSS file static/src/main.scss is set up as the main entrypoint for the index view and can be used on the detail view as well.
- Use modern CSS best practices.
- If you know SCSS you may use SCSS features where appropriate, but they are not required.
- No designs are provided. Do your best to make these basic pages visually appealing.
> Done

## AI usage
I consulted AI for learning how functions worked, such as the syntax/how functions work in Django, as I previously mentioned this is my first time using Django. I also used AI to troubleshoot when I was having errors, such as diagnosing the UUIDField issue I had in models.py 

## Final thoughts
If anyone reads this I'm pleasantly surprised! This was extremely fun to complete, as this is my first time using Django and even sqlite3. To stay anonymous best I can, I use a different Python library for web dev and use a server based SQL db, so it was so fun learning Django and SQLite 3 whilst doing this exercise. I definitely will use these technologies for some web app ideas I have!

Thank you so much for this opportunity! I'm extremely grateful :)