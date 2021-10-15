---
layout: page
title: COVID-19 in the Bay Area
permalink: /covid/
---

# Bay Area COVID-19 Dashboard

![](https://img.shields.io/badge/dynamic/yaml?color=informational&label=Plots%20Last%20Updated&query=date&url=https%3A%2F%2Fraw.githubusercontent.com%2Fslwatkins%2Fcovid%2Fmaster%2F.github%2Fdate_last_updated.yml)

This page is a mirror of the `README` in the [slwatkins/covid]() GitHub repository. The repo was intended for simple plotting and analyzing COVID-19 cases/deaths, with a focus on the San Francisco Bay Area. The data in the plots below are from the [John Hopkins University dataset](https://github.com/CSSEGISandData/COVID-19). The plots below are easily reproducible using the Python code in the repo (which has been organized as an installable package). The package also has useful functions for reading in the COVID-19 data from both the JHU and [NY Times](https://github.com/nytimes/covid-19-data) datasets.

The Bay Area counties included are:
 * Alameda
 * Contra Costa
 * Marin
 * Napa
 * San Francisco
 * San Mateo
 * Santa Clara
 * Solano
 * Sonoma

## Current Bay Area Numbers

Below, we show the total, cumulative cases (and deaths) over time for the combined 9 Bay Area counties.

![Bay Area Cumulative](https://raw.githubusercontent.com/slwatkins/covid/master/.github/current_bay_area_total_cases.png)

Below, we show the daily new cases (and deaths) over time for the combined 9 Bay Area counties.

![Bay Area Daily](https://raw.githubusercontent.com/slwatkins/covid/master/.github/current_bay_area_new_cases.png)

## County-by-County Numbers

Below, we show the total, cumulative cases (and deaths) over time for each of the 9 Bay Area counties.

![County Cumulative](https://raw.githubusercontent.com/slwatkins/covid/master/.github/current_county_total_cases.png)

Below, we show the daily new cases over time for each of the 9 Bay Area counties.

![County Daily](https://raw.githubusercontent.com/slwatkins/covid/master/.github/current_county_new_cases.png)

Below, we show the daily new cases over the last month for each of the 9 Bay Area counties.

![County Daily, Recent](https://raw.githubusercontent.com/slwatkins/covid/master/.github/current_county_new_cases_month.png)
