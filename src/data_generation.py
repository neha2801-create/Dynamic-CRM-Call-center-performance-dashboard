import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import secrets

def generate_call_data(num_weeks=52):
    dates = [(datetime.now() - timedelta(weeks=x)).strftime('%Y-%m-%d') for x in range(num_weeks)]
    
    data = {
        'week': dates,
        'total_calls': np.random.randint(100, 500, num_weeks),
        'resolved_calls': [],
        'average_resolution_time': np.random.uniform(10, 60, num_weeks).round(2),
        'customer_satisfaction': np.random.uniform(3.0, 5.0, num_weeks).round(2),
        'escalated_calls': np.random.randint(5, 50, num_weeks)
    }
    
    for total in data['total_calls']:
        data['resolved_calls'].append(secrets.SystemRandom().randint(int(total * 0.7), total))

    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/call_data.csv', index=False)
    return df

if __name__ == "__main__":
    generate_call_data()
    print("Call center data generated successfully!")
