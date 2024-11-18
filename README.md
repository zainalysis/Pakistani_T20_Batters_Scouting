# Analysis of Pakistani Batters Talent Pool

This repository contains a data-driven analysis of the talent pool of Pakistani batters, identifying the most suitable players for the playing XI.

## Files

- **pakistan_batters_analysis.ipynb**: Jupyter Notebook with all code and analysis.
- **average_pattern_lengths_pakistan_qualified.csv**: CSV file with the average pattern lengths of consecutive 0s and 1s in the batters' performances.
- **average_balls_between_boundaries_pakistan.csv**: CSV file showing the average number of balls between boundaries (4s or 6s) for qualified batters.

## Methodology
- Filtered data for Pakistani batters who played at least 20 unique matches.
- Calculated patterns in scoring (0s and 1s) and boundary intervals to evaluate consistency and explosiveness.

# Pakistani Batters Talent Pool Analysis

This project analyzes the talent pool of Pakistani batters to identify players who should be part of the playing eleven. The analysis focuses on batting performances using advanced metrics such as:
- Average length of consecutive low scores (0s or 1s).
- Average balls between boundaries (4s or 6s).

## Dataset Information

- **Size:** The dataset contains over **1.8 million rows** with ball-by-ball details of cricket matches.
- **Features:** More than 60 attributes, including batting, bowling, and match-specific details.
- **Source:** The dataset is owned by [Himanish Ganjoo](https://twitter.com/himanishganjoo). Credit and thanks to @himanishganjoo for sharing this comprehensive dataset.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.


## Requirements
- Python 3.7+
- pandas library

## How to Use
1. Clone the repository.
2. Open the `.ipynb` file in Jupyter Notebook or Google Colab.
3. Run the notebook to reproduce the analysis.

