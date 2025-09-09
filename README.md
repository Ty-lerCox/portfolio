# Portfolio

Static portfolio powered by GitHub Pages + Jekyll.

## Local preview
```bash
bundle install
bundle exec jekyll serve
```

## Configure
- Set `url` and `baseurl` in `_config.yml`.
- Replace SVG placeholders in `assets/img/` with real images.
- Update links to your GitHub/LinkedIn/email in `index.md` and `resume/index.md`.
- (Optional) Update `analytics.google.id` in `_config.yml` with your Google Analytics Measurement ID.

## Structure
See `projects/`, `resume/`, and `assets/` for content organization.

## ATS Prompt Generator
Use `generate_ats_prompt.py` to combine a job post and one or more resume
text files into a ready-to-use prompt for ATS keyword analysis.

```bash
python generate_ats_prompt.py job.txt resume.txt
```

Prompts are written to the `ats_prompts/` directory.

