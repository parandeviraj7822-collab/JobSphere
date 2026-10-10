from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JobSphere - Smart Student Job Portal</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: Arial, sans-serif;
    color: white;
    background: linear-gradient(135deg, #10152f, #243b70, #512b81);
    min-height: 100vh;
}
nav {
    padding: 22px 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #10152f88;
}
.logo { font-size: 27px; font-weight: bold; color: #66e3ff; }
nav a { color: white; text-decoration: none; margin-left: 20px; }
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 40px;
    padding: 70px 8%;
    flex-wrap: wrap;
}
.content { max-width: 600px; }
h1 { font-size: clamp(40px, 6vw, 65px); margin-bottom: 20px; }
h1 span { color: #66e3ff; }
p { font-size: 18px; line-height: 1.7; color: #e0e6ff; }
button {
    border: none;
    border-radius: 10px;
    padding: 14px 24px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    margin: 10px 8px 0 0;
}
.primary { background: #66e3ff; color: #10152f; }
.secondary { background: transparent; color: white; border: 1px solid white; }
.robot {
    font-size: 130px;
    text-align: center;
    padding: 35px;
    border: 1px solid #ffffff44;
    border-radius: 30px;
    background: #ffffff12;
    box-shadow: 0 0 45px #66e3ff22;
}
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px 8% 60px;
}
.card {
    background: #ffffff12;
    border: 1px solid #ffffff22;
    border-radius: 18px;
    padding: 25px;
}
.card h3 { color: #66e3ff; }
footer { text-align: center; padding: 25px; color: #d2d9ff; }
</style>
</head>
<body>
<nav>
    <div class="logo">🚀 JobSphere</div>
    <div><a href="#home">Home</a><a href="#features">Features</a></div>
</nav>
<section class="hero" id="home">
    <div class="content">
        <p>✨ YOUR CAREER STARTS HERE</p>
        <h1>Find Your <span>Dream Job</span></h1>
        <p>Welcome to JobSphere — a smart student job portal
        designed to help students explore internships, discover
        opportunities and take the first step toward their careers.</p>
        <button class="primary" onclick="showMessage()">Get Started →</button>
        <button class="secondary" onclick="document.getElementById('features').scrollIntoView({behavior:'smooth'})">Explore Features</button>
    </div>
    <div class="robot">🤖<p>YOUR AI CAREER BUDDY</p></div>
</section>
<section class="cards" id="features">
    <div class="card"><h3>🎯 Smart Opportunities</h3><p>Explore job and internship opportunities for students.</p></div>
    <div class="card"><h3>📄 Career Profile</h3><p>Prepare to present your skills and qualifications.</p></div>
    <div class="card"><h3>🌟 Career Growth</h3><p>Discover new paths to build your future.</p></div>
</section>
<footer>© 2026 JobSphere | Smart Student Job Portal</footer>
<script>
function showMessage() {
    alert("Welcome to JobSphere! Registration and login are coming soon.");
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)