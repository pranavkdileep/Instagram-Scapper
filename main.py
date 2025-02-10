import requests
import json
import csv
from instagrapi import Client

cl = Client()
cl.login('pnv8.pvt', 'pass')

xrapidapikey = "50c9c3f974msh08092f88f044eedp10a9f2jsnfaf6222bc9c6"

def getUernames():
    datafile = open("usernames.csv", "w")
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Username", "Full Name", "Is Private", "Has Opt Eligible Shop","follower_count","links","biography","public_email","contact_phone_number","public_phone_number","business_contact_method"])
    keywords = []
    while True:
        keyword = input("Enter keyword: ")
        if keyword == "":
            break
        keywords.append(keyword)
    url = "https://rocketapi-for-instagram.p.rapidapi.com/instagram/search"
    headers = {
        "x-rapidapi-key": "50c9c3f974msh08092f88f044eedp10a9f2jsnfaf6222bc9c6",
        "x-rapidapi-host": "rocketapi-for-instagram.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    for keyword in keywords:
        querystring = { "query": keyword }
        response = requests.post(url, headers=headers, json=querystring)
        response = response.json()
        #print(response)
        if response['status'] == "done":
            print("Done")
            body = response['response']['body']
            users = body['users']
            for user in users:
                try :
                    userdetails = cl.user_info_by_username(user['user']['username'])
                    follower_count = userdetails.follower_count
                    biography = userdetails.biography
                    public_email = userdetails.public_email
                    contact_phone_number = userdetails.contact_phone_number
                    public_phone_number = userdetails.public_phone_number
                    business_contact_method = userdetails.business_contact_method
                    bio_links = userdetails.bio_links
                    linkarr = []
                    for link in bio_links:
                        linkarr.append(link.url)
                except:
                    follower_count = "NA"
                    biography = "NA"
                    public_email = "NA"
                    contact_phone_number = "NA"
                    public_phone_number = "NA"
                    business_contact_method = "NA"
                    linkarr = "NA"
                print(userdetails)
                print(user['user']['username'])
                print(user['user']['full_name'])
                print(user['user']['is_private'])
                print(user['user']['has_opt_eligible_shop'])
                csvwriter.writerow([user['user']['username'], user['user']['full_name'], user['user']['is_private'], user['user']['has_opt_eligible_shop'],follower_count,linkarr,biography,public_email,contact_phone_number,public_phone_number,business_contact_method])


getUernames()

