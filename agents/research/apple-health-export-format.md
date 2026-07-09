# Apple Health Export Format Research

Access date: 2026-07-09

## Research Questions

- What does Apple officially document about exporting Health data?
- What files and structures are commonly observed in Apple Health exports?
- Which parts of the export format must be treated as assumptions until the founder's real export is inspected?
- What parsing and privacy constraints should shape the first local importer?

## Sources Consulted

### Apple Support: Share your data in Health on iPhone

- Source: Apple Support
- URL: https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios
- Finding: Apple documents that users can export all health and fitness data from the Health app in XML format by using "Export All Health Data."
- Classification: documented behavior.

### In Defence of XML: Exporting and Analysing Apple Health Data

- Source: TDDA technical article
- URL: https://www.tdda.info/in-defence-of-xml-exporting-and-analysing-apple-health-data
- Finding: Community-observed exports include an XML document with top-level health data elements such as records, workouts, and activity summaries. The article also highlights that exports may be large.
- Classification: trustworthy technical observation, not Apple schema documentation.

### Apple Health Export Part I

- Source: R-bloggers technical walkthrough
- URL: https://www.r-bloggers.com/2020/02/apple-health-export-part-i/
- Finding: Community-observed XML categories include `Record`, `ActivitySummary`, `Workout`, and clinical records. Some expanded exports may include workout route files, ECGs, or clinical records depending on user data.
- Classification: trustworthy technical observation, not Apple schema documentation.

### Apple Support Community discussions

- Source: Apple Support Community
- URL: https://discussions.apple.com/thread/254202523
- Finding: Users have reported parsing problems across iOS versions, reinforcing that the importer should not assume every export is identical or perfectly formed for strict XML tooling.
- Classification: user-reported behavior; useful risk signal, not authoritative specification.

## Documented Behavior

- Apple provides a user-facing "Export All Health Data" flow from the Health app.
- Apple describes the exported data as XML.
- The export contains health and fitness data and is sensitive personal information.

## Observed Export Structure

Observed by technical community sources, pending validation against the founder's real export:

```text
export.zip
  apple_health_export/
    export.xml
    export_cda.xml                 # may exist when clinical records are present
    workout-routes/                # may exist when workouts include routes
      route_*.gpx                  # naming may vary
    electrocardiograms/            # may exist for ECG data
```

Commonly observed `export.xml` element families:

- `HealthData`
- `Record`
- `ActivitySummary`
- `Workout`
- `WorkoutEvent`
- `MetadataEntry`
- `ClinicalRecord`

Commonly observed attributes:

- `type`
- `sourceName`
- `sourceVersion`
- `device`
- `unit`
- `creationDate`
- `startDate`
- `endDate`
- `value`
- workout attributes such as activity type, duration, duration unit, distance, distance unit, and energy burned where present.

## Assumptions

- The founder's export will include `export.xml`.
- The export may include workout route GPX files if route data exists.
- Dates may include timezone offsets and should be parsed as timezone-aware values.
- The export may be large enough to require streaming XML parsing.
- Source and device strings are not stable identifiers and may vary by OS, device, app, and locale.

## Unknowns

- Exact archive folder name from the founder's current iOS version.
- Whether `export_cda.xml`, workout routes, ECGs, or clinical records are present.
- Whether route files can be reliably linked to `Workout` entries without inspecting real filenames and attributes.
- Whether all relevant running metrics appear as `Record` rows, workout metadata, route files, or a combination.
- Whether malformed XML or DTD issues appear in the founder's export.
- Real file size, record count, and memory constraints.

## Importer Consequences

- Inspect the archive structure before assuming paths.
- Use streaming XML parsing for `export.xml`; do not load the whole file into memory by default.
- Start with Python standard library tools such as `zipfile`, `xml.etree.ElementTree.iterparse`, `sqlite3`, `datetime`, and `pathlib`.
- Produce a safe inventory before detailed normalization.
- Treat raw import, normalization, and analytics as separate stages.
- Store raw source fidelity without exposing raw health samples to the dashboard.

## Privacy Consequences

- The real export must stay outside Git.
- GPX route files must stay outside Git because they can reveal home, work, and running locations.
- Documentation may include only safe summaries, never raw records or coordinates.
- Synthetic fixtures should be created later by hand or generated from representative structures, not by redacting the founder's real export unless explicitly reviewed.
