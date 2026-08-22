# Governance

## Pack verification levels

Every jurisdiction pack, court-rule pack, or rubric declares one of:

```
EXPERIMENTAL       , schema/structure only, no content verified
COMMUNITY REVIEWED  , a named contributor supplied primary sources; not
                       independently re-checked by a maintainer
SPECIALIST REVIEWED , checked by someone with relevant subject-matter
                       qualification (named, with their basis for review stated)
MAINTAINER VERIFIED , a repository maintainer re-checked every primary
                       source cited and can stand behind the pack's accuracy
                       as of its stated verification date
```

No pack may claim a level it hasn't earned. Do not invent institutional or professional endorsement, see `docs/SPEC_FULL_TEXT.md` Part CLXII.

## Merging jurisdiction or court content

A pull request touching `jurisdictions/`, `courts/`, `regulators/`, `citation/`, or `rubrics/` must include, per proposition changed:

- the primary source (official site, official publication, or a named secondary source if no primary source is public)
- the date the source was checked
- the reviewer's name
- what test case (if any) exercises the change

Markdown compiling is not sufficient grounds for merge, see `docs/SPEC_FULL_TEXT.md` Part CLX.

## Decision process

Until this project has more than one active maintainer, decisions are made by whoever is actively maintaining the repository, applying the rules above as the actual constraint, not by vote. As the contributor base grows, this file will be updated to describe a real review/maintainer structure rather than asserting one that doesn't exist yet.

## Reporting a governance or accuracy problem

Open an issue tagged `accuracy` for anything you believe is wrong in a jurisdiction pack, citation, or procedural claim, these get priority over feature requests, consistent with the project's own hard-failure rules.
