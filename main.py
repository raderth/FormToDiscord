from flask import Flask, render_template, request
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = "your url"

app = Flask(__name__)
    

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST": #on form submission
        username = request.form["username"]
        age = request.form["age"]
        country = request.form["country"]
        play = request.form["play"] #how often are you likely to play?
        join = request.form["join"] #why would you like to join?
        fav = request.form["fav"] #favourite aspect of Minecraft?
        discord = request.form["discord"] #do you use Discord a lot?
        mature = request.form["mature"]
        smp = request.form["smp"] #previous smp(s)
        time = request.form["time"] #how long have you been playing Minecraft
        guidelines = request.form["guidelines"]

        

        if guidelines == "on":
          guidelines = "Yes"
        else:
          guidelines = "No"
      
        webhook = DiscordWebhook(url=webhook_url)
        
        # create embed object for webhook
        embed = DiscordEmbed(title='Form Submission', color='03b2f8')
        
        # set timestamp (default is now)
        embed.set_timestamp()
        
        # add fields to embed
        embed.add_embed_field(name='Username', value=username)
        embed.add_embed_field(name='Age', value=age)
        embed.add_embed_field(name='Location', value=country)
        embed.add_embed_field(name='How often they play', value=play)
        embed.add_embed_field(name='Why they want to join', value=join, inline=False)
        embed.add_embed_field(name='Favourite aspect of Minecraft', value=fav, inline=False)
        embed.add_embed_field(name='Discord usage', value=discord)
        embed.add_embed_field(name='Are they mature?', value=mature)
        embed.add_embed_field(name='Previous Smp', value=smp, inline=False)
        embed.add_embed_field(name='How long they have played', value=time)
        embed.add_embed_field(name='Read and accepted Guidelines', value=guidelines)
        
        # add embed object to webhook
        webhook.add_embed(embed)
        
        response = webhook.execute()

        return render_template("success.html")

    else:
      return render_template("form.html")

app.run(host='0.0.0.0', port=81)
