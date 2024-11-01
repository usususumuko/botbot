import os

# Install required Python packages
os.system("pip3 install cloudscraper")
os.system("pip3 install socks")
os.system("pip3 install pysocks")
os.system("pip3 install colorama")
os.system("pip3 install undetected_chromedriver")
os.system("pip3 install httpx")

# Download and install Google Chrome
os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
os.system("apt-get install -y ./google-chrome-stable_current_amd64.deb")
os.system("rm google-chrome-stable_current_amd64.deb")  # Clean up

# Download additional files
os.system("wget https://raw.githubusercontent.com/usususumuko/botbot/main/bot.py")
os.system("wget https://raw.githubusercontent.com/usususumuko/botbot/main/ua.txt")
os.system("wget https://raw.githubusercontent.com/usususumuko/botbot/main/proxy.txt")

print("Done.")
