from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# HTML+CSS+JS inside a single Flask file
dashboard_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to your Wealth Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #264653;
            color: white;
            padding: 20px;
            text-align: center;
        }
        main {
            padding: 30px;
            max-width: 1100px;
            margin: auto;
        }
        .card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }
        h2 {
            margin-top: 0;
            color: #264653;
        }
        .btn {
            background-color: #264653;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: #2a9d8f;
        }
        canvas {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Your Wealth Dashboard</h1>
    </header>

    <main>
        <div class="card">
            <h2>Portfolio Summary</h2>
            <ul>
                <li>💰 Cash: $10,000</li>
                <li>📈 Stocks: $25,000</li>
                <li>🏠 Real Estate: $40,000</li>
                <li>⚖️ Bonds: $15,000</li>
            </ul>
            <canvas id="portfolioChart" width="200" height="200"></canvas>
        </div>

        <div class="card">
            <h2>Portfolio Growth Trend</h2>
            <canvas id="growthChart" width="300" height="250"></canvas>
        </div>

        <div class="card">
            <h2>Net Worth</h2>
            <p style="font-size: 24px;"><strong>$90,000</strong></p>
        </div>

        <div class="card">
            <h2>Upcoming Actions</h2>
            <ul>
                <li>📅 Rebalance Portfolio - {{ rebalance_date }}</li>
                <li>📅 Tax Planning Session - {{ tax_date }}</li>
                <li>📅 Mutual Fund SIP - {{ sip_date }}</li>
            </ul>
        </div>

        <div class="card">
            <h2>Risk Profile: Moderate</h2>
            <form method="POST" action="/advice">
                <button class="btn">Get Investment Advice</button>
            </form>
            {% if advice %}
                <p style="margin-top: 15px;">🧠 {{ advice }}</p>
            {% endif %}
        </div>
    </main>

    <script>
        // Portfolio Pie Chart
        new Chart(document.getElementById('portfolioChart'), {
    		type: 'pie',
   		data: {
       			 labels: ['Cash', 'Stocks', 'Real Estate', 'Bonds'],
       			 datasets: [{
           			 label: 'Portfolio',
          		  	 data: [10000, 25000, 40000, 15000],
            			 backgroundColor: ['#e76f51', '#2a9d8f', '#f4a261', '#264653']
        		      }]
   	 	},
    		options: {
       			 responsive: false,
       			 maintainAspectRatio: false
   		}
	});

        // Growth Line Chart
        new Chart(document.getElementById('growthChart'), {
    		type: 'line',
    		data: {
        		labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        		datasets: [{
            			label: 'Portfolio Value ($)',
            			data: [65000, 68000, 72000, 74000, 80000, 90000],
            			borderColor: '#2a9d8f',
            			fill: false,
            			tension: 0.3
        		}]
    		},
   		options: {
        		responsive: false,
        		maintainAspectRatio: false
    		}
	});
    </script>
</body>
</html>
'''

# 🏠 Main dashboard route
@app.route('/', methods=['GET'])
def dashboard():
    today = datetime.date.today()
    return render_template_string(
        dashboard_template,
        rebalance_date=today.replace(day=15).strftime("%B %d, %Y"),
        tax_date=(today.replace(month=12, day=1)).strftime("%B %d, %Y"),
        sip_date=(today + datetime.timedelta(days=30)).strftime("%B %d, %Y"),
        advice=None
    )

# 🧠 AI-like advice (static for now)
@app.route('/advice', methods=['POST'])
def give_advice():
    today = datetime.date.today()
    advice = "Consider adding index funds and reducing exposure to volatile assets. Explore international ETFs for diversification."
    return render_template_string(
        dashboard_template,
        rebalance_date=today.replace(day=15).strftime("%B %d, %Y"),
        tax_date=(today.replace(month=12, day=1)).strftime("%B %d, %Y"),
        sip_date=(today + datetime.timedelta(days=30)).strftime("%B %d, %Y"),
        advice=advice
    )

# ▶️ Run on PORT 5014
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5014, debug=True)