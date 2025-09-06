#!/usr/bin/env python3
"""Generate ATS keyword-analysis prompts from a job post and resume(s).

The script reads a job description file and one or more resume text files and
creates a prompt combining them. Each resulting prompt mirrors the template
used for ATS keyword analysis and is written to an output directory.

Usage:
    python generate_ats_prompt.py job.txt resume1.txt [resume2.txt ...]
"""

from __future__ import annotations

import argparse
from pathlib import Path

PROMPT_TEMPLATE = """You are my ATS keyword & resume tailor.

GOAL
Maximize alignment between my resume and the target job post without making false claims, while keeping an ATS-safe format.

INPUTS
[JOB POST]
<<< {job_description} >>>

[RESUME]
<<< {resume} >>>

OUTPUT (in this exact order)
1) KEYWORDS_JSON
   - JSON with:
     {{
       "hard_skills": [{{"term":"React", "weight":5, "synonyms":["React.js"]}}, ...],
       "tools": [{{"term":"Azure DevOps","weight":4,"synonyms":["ADO","Azure Boards"]}}],
       "languages": [...],
       "cloud": [...],
       "soft_skills": [...],
       "certs_or_quals": [...],
       "domain_terms": [...],
       "must_haves": [...],   // legal/clearance/shift/location/degree-alt
       "nice_to_haves": [...]
     }}
   - Weights: 5=critical, 4=important, 3=useful, 2=minor, 1=nice.

2) COVERAGE_TABLE
   - A compact table listing each keyword → Present/Missing → Where found or suggested placement.
   - Map synonyms (e.g., “CI/CD” covers “continuous integration”, etc.).

3) EDIT_SUGGESTIONS
   - Bullet-by-bullet rewrites (STAR-style) that truthfully incorporate missing/aligned keywords.
   - Keep metrics, impact, and tense consistent. No fluff, no exaggerations.

4) SUMMARY + SKILLS
   - 2–3 line Professional Summary tailored to the job.
   - ATS-friendly SKILLS block grouping the critical keywords.

5) REVISED_RESUME (ATS-safe)
   - Single column, no text boxes/tables, standard headings (SUMMARY, SKILLS, EXPERIENCE, EDUCATION).
   - Integrate approved rewrites and keyword coverage naturally.
   - Keep everything truthful and consistent with my background.

6) MATCH_SCORE
   - % coverage using your weights. Show formula and top gaps to close the last 10–20%.
"""


def generate_prompt(job_text: str, resume_text: str) -> str:
    """Return the ATS prompt with inserted job description and resume."""
    return PROMPT_TEMPLATE.format(
        job_description=job_text.strip(), resume=resume_text.strip()
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate ATS keyword analysis prompts."
    )
    parser.add_argument(
        "job", type=Path, help="Path to job description text file."
    )
    parser.add_argument(
        "resumes",
        type=Path,
        nargs="+",
        help="Path(s) to resume text file(s).",
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        type=Path,
        default=Path("ats_prompts"),
        help="Directory where prompt files will be written.",
    )
    args = parser.parse_args()

    job_text = args.job.read_text(encoding="utf-8")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for resume_path in args.resumes:
        resume_text = resume_path.read_text(encoding="utf-8")
        prompt = generate_prompt(job_text, resume_text)
        out_path = args.out_dir / f"{resume_path.stem}_prompt.txt"
        out_path.write_text(prompt, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
