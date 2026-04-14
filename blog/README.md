# Strata Properties Blog

A personal blog about the daily frustrations of being a Strata Chairperson in NSW and building an app to solve some of them.  
Built with [Hugo](https://gohugo.io/).

## Prerequisites

- [Hugo](https://gohugo.io/installation/) v0.159 or later (extended edition)

## Development

Start the local development server with live reload:

```sh
hugo server
```

The site will be available at http://localhost:1313.

To include draft posts:

```sh
hugo server -D
```

## Writing Posts

Create a new post from the archetype template:

```sh
hugo new content posts/YYYY-MM-DD.md
```

Edit the generated file in `content/posts/`. Set `draft: false` when the post is ready to publish.

## Building

Generate the static site into the `public/` directory:

```sh
hugo
```

The `public/` directory is excluded from version control — deploy its contents to your web host.

## Project Structure

```
archetypes/   Content templates for new posts
assets/css/   Source CSS (processed and fingerprinted by Hugo)
content/      Markdown content
  posts/      Blog posts (date-named files)
  about.md    About/disclaimer page
layouts/      HTML templates
static/       Static files (logo, favicon)
```

## Deployment

Build with `hugo` and upload the `public/` directory to your static web host.

## Article Ideas

* the structure of fire safety - the schedule, alarms, engineers, practitioners, AFSS, etc.
* sell the lot - redevelopment/strata renewal
* waterproofing - balconies and planters and DAs and CDCs
* water levies - individual and collective water bills
