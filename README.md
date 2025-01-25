# Call Center CRM Dashboard

## Problem Statement
Call centers face challenges in:
- Tracking resolution rates across different time periods
- Monitoring customer satisfaction trends
- Managing call volumes and escalations
- Measuring agent performance
- Real-time decision making based on KPIs

## Purpose
This dashboard provides real-time visualization of call center metrics to:
- Improve response times
- Reduce escalation rates
- Enhance customer satisfaction
- Optimize resource allocation
- Track performance trends

## Process Flow
1. Data Generation → Processing → Visualization → Analysis
2. Weekly metrics calculation and trend analysis
3. Real-time KPI monitoring and alerts
4. Interactive filtering and drill-down capabilities

## File Structure and Purpose
```
call-center-crm/
├── data/
│   └── call_data.csv          # Generated sample call center data
│                              # Contains: dates, call volumes, resolution times,
│                              # satisfaction scores, escalation counts
├── src/
│   ├── data_generator.py      # Generates synthetic call center data
│   │                          # - Creates weekly call records
│   │                          # - Simulates realistic metrics
│   │                          # - Handles data storage
│   │
│   └── dashboard.py           # Main Streamlit dashboard application
│                              # - Loads and processes data
│                              # - Creates interactive visualizations
│                              # - Displays real-time KPIs
│
└── requirements.txt           # Project dependencies
```

## Implementation Steps

### 1. Setup
```bash
git clone <repo-url>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Data Generation
```bash
python src/data_generator.py
```
Generates:
- 52 weeks of call data
- Random but realistic metrics
- CSV file in data directory

### 3. Dashboard Launch
```bash
streamlit run src/dashboard.py
```
Features:
- Interactive metrics
- Time-series visualizations
- KPI tracking
- Performance analysis

## Key Metrics Tracked
1. Resolution Metrics
   - Weekly resolution rate
   - Average resolution time
   - First-call resolution rate

2. Customer Experience
   - Satisfaction scores
   - Escalation rates
   - Feedback trends

3. Volume Analysis
   - Call patterns
   - Peak periods
   - Resource utilization

## Technical Details

### Data Generator
- Simulates realistic call center data
- Configurable parameters for data generation
- Built-in data validation

### Dashboard Components
- Real-time metric calculations
- Interactive Plotly visualizations
- Streamlit widgets for filtering
- Responsive layout

## Future Enhancements
1. Additional Features
   - Agent performance tracking
   - Predictive analytics
   - Custom reporting
   - Alert system

2. Technical Improvements
   - Database integration
   - API endpoints
   - Advanced analytics
   - Mobile optimization

## Requirements
- Python 3.9+
- See requirements.txt for package details

## License
MIT License