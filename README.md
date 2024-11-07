# Benford 2024 Election Analysis with Python

## Overview
The **Benford 2024 Election Analysis** project leverages Benford's Law to analyze the voting data of the 2024 U.S. Presidential Election. Benford's Law, often used in data science for fraud detection, predicts the distribution of first digits in numerical datasets. By comparing the first digits of election vote counts to the theoretical distribution of Benford's Law, we can assess the authenticity of the voting data.

## Purpose
The goal of this analysis is to:
- **Evaluate the fairness of the election results** by comparing actual vote counts to the expected distribution.
- **Identify any irregularities or anomalies** that could suggest tampering or inconsistencies in the reported vote counts.
- **Provide insights into election transparency** using statistical methods.

- ![Ekran Görüntüsü (53)](https://github.com/user-attachments/assets/a48a0ed9-7a0a-4dd2-8428-27cd29f647c0)

## Methodology
1. **Data Collection**: Vote data for major candidates (e.g., Trump, Kamala Harris) is extracted from publicly available election results.
2. **Benford's Law**: We compute the first-digit distribution for the vote counts and compare it to the expected distribution.
3. **Chi-Square Test**: We use statistical analysis to quantify any deviation from the expected Benford distribution.

## How to Use
1. Download or access the election data in CSV format.
2. Ensure the data includes numerical vote counts for each candidate.
3. Run the analysis using Python. The analysis will output:
   - A comparison of the observed first-digit distribution versus Benford's expected distribution.
   - A Chi-square test statistic to assess how closely the data follows Benford's Law.

## Requirements
- Python 3.x
- `pandas`, `numpy`, `matplotlib`, `scipy` libraries
- A CSV file with election vote counts

## Results
The outcome of the analysis will provide a statistical measure of whether the election data follows the expected distribution. If significant deviations are found, further investigation may be warranted.

## Conclusion
By applying Benford's Law to the 2024 U.S. Election data, we can gain a deeper understanding of potential data anomalies and enhance the transparency and credibility of the election results.

## Sources
- **The Telegraph** - "2024 U.S. Presidential Election: Harris vs. Trump Latest Results"  
  [Read more on The Telegraph](https://www.telegraph.co.uk/us-election/presidential-election-2024-harris-trump-latest-results/)
  
## License
This project is open-source and available under the MIT License.
