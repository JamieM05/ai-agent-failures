# Contributing

Thanks for helping build the database. The bar is **verifiable and in your own words**.

1. **Check it is a real, public incident.** Find at least one reliable public source; two or more for `verified_multiple_secondary`. A court, regulator or company statement counts as primary.
2. **Add one YAML file** in `incidents/`, named `YYYY-MM-short-name.yaml`, with `id` equal to the file name. Copy an existing entry as a template.
3. **Write in your own words.** Do not paste or closely paraphrase article text. Short quotation of a few words is fine; long quotes are rejected by the validator.
4. **Be honest about uncertainty.** Say who established the root cause (`root_cause.attribution`), give a `basis` and `confidence` for any loss figure, and use `notes` for caveats (single-source, unread pages, disputed claims). Do not guess model names.
5. **Tag failure modes** using ids in `taxonomy/failure-modes.yaml`. If you add an incident to a mode, run `python scripts/gen_taxonomy_md.py` after updating that mode's `example_incidents` list (the validator checks the two stay in sync).
6. **Validate:** `pip install -r scripts/requirements.txt && python scripts/validate.py`.
7. **Open a pull request** (or use the *New incident* issue template if you only have the sources).

Rights: by contributing you agree your contribution is licensed under the repository's MIT licence and that you have not copied material you do not have the right to share.
