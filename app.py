from flask import Flask, render_template, request

app = Flask(__name__)

# List of parties
parties = ["Party A", "Party B", "Party C", "Party D", "Party E", "Party F", "Party G", "Party H"]

# Dictionary to store votes
votes = {party: 0 for party in parties}

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        party = request.form.get("party")
        if party in votes:
            votes[party] += 1
    total_votes = sum(votes.values())
    return render_template("index.html", parties=parties, votes=votes, total_votes=total_votes)

@app.route("/update_vote", methods=["POST"])
def update_vote():
    party_action = request.form.get("party")
    if party_action:
        party, action = party_action.rsplit("-", 1)
        if party in votes:
            if action == "increase":
                votes[party] += 1
            elif action == "decrease" and votes[party] > 0:
                votes[party] -= 1
    total_votes = sum(votes.values())
    return render_template("index.html", parties=parties, votes=votes, total_votes=total_votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

