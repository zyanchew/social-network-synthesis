# Social network analysis project
This research project explore the influence of social networks on travel behavior, specifically synthesize social interaction between individuals and their social network members with various joint activities. The composition and dynamics of social networks are investigated through two models:

### Model I: Social Network Composition and Joint Activities
Model I examines:
- The overall composition and size of social networks.
- Frequency of joint activities with social network members.
- Impact of socio-demographic characteristics on network size and activity frequency.

**Key Variables**:
- Individual socio-demographic characteristics.
- Social network size for each social category (e.g., friends, colleagues).
- Frequency of activities across all network members.

### Model II: Relationship Dynamics and Joint Activities
Model II explores:
- How differences (or similarities) between egos and alters influence joint activity frequency.
- The impact of gender, age, education differences, geographical distance, relationship duration, and social categories.

**Key Variables**:
- Differences in gender, age, education, geographical distance, and relationship duration.
- Social relationship types and joint activity frequencies.

## Directory Structure
- `data/`: Stores raw datasets.
- `results/`: Generated tables, figures, and analysis outputs.
  -`figures/`: Generated graphs.
  -`tables/`: Generated tables.
- `src/`: Python scripts for data processing, analysis, and visualization.
  - `data.py`: Descriptive statistics.
  - `aggregate.py`: Recalculates variables for Model 1.
  - `plot_model1.py`: Analyzes and visualizes Model 1 data.
  - `plot_model2.py`: Analyzes and visualizes Model 2 data.
- `README.md`: Project description.
