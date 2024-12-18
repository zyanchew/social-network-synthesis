# Social network analysis project
This research project aims to explore the influence of social networks on travel behavior, specifically how social interaction between individuals and their social network members would influence the frequency of various joint activities. The composition and dynamics of social networks are investigated through two models:

### Model I: Social Network Size, Composition and Joint Activities at Ego Level
Model I examines:
- The overall composition and size of social networks.
- Frequency intervals of joint activities with all social network members.
- Impact of socio-demographic characteristics on network size and activity frequency.

**Key Variables**:
- Individual socio-demographic characteristics.
- Social network size for each social category (e.g., friends, colleagues).
- Frequency of joint activities.

### Model II: Social Relationships and Joint Activities at Ego-Alter Level
Model II explores:
- How differences (or similarities) between egos and alters influence joint activity frequency.
- The impact of gender, age, education differences, geographical distance, relationship duration, and social categories on joint activity frequency.

**Key Variables**:
- Differences in gender, age, education, geographical distance, and relationship duration.
- Social relationship types and joint activity frequencies.

## Directory Structure
- `data/`: Stores raw datasets.
- `bbn/`: Stores the developed models.
- `ref/`: Figures that referenced in README.md.
- `results/`: Generated tables, figures, and analysis outputs.
  -`figures/`: Generated graphs.
  -`tables/`: Generated tables.
- `src/`: Python scripts for data processing, analysis, and visualization.
  - `data.py`: Descriptive statistics.
  - `aggregate.py`: Recalculates variables for Model 1.
  - `plot_model1.py`: Analyzes and visualizes Model 1 data.
  - `plot_model2.py`: Analyzes and visualizes Model 2 data.
- `README.md`: Project description.


## Methodology
This research employed Bayesian Belief Networks to model the interdependencies between social network and travel behavior using GeNIe software. The conceptual framework for this research project:

[Concentual Framework](ref/con_framework.png)

Model I systhesize individual's socio-demographic characteristics, composition, size of social networks with joint activities frequecies to study the relationships among them at ego level. While Model II emphasize a disaggregated perspective of social interaction, which synthesize ego's and alter's socio-demographic characteristics, homophily/heterogeinety in social relationship, social relationship types and joint activity frequency. 

## Results

