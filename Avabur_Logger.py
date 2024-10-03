# Import Statements
import os
from datetime import datetime
from datetime import timedelta
from urllib.request import Request, urlopen
from dotenv import load_dotenv
import gspread
import json
import ssl

# Start of Main() Funcion
def main():
    load_dotenv()
    WB = os.getenv('WORKBOOK')
    DB = os.getenv('DATABASE')
    CD = os.getenv('CDATA')
    CDB = os.getenv('CDATABASE')
    URL_LINK = os.getenv('SECRET_CODE')

    # Initialize some variables
    timeshift = 5+(2/86400)
    now = datetime.now()+timedelta(hours=timeshift)
    myDateTime = now.strftime("%Y%m%d_%H%M%S")
    myDate = now.strftime("%Y%m%d")

    # Start the Connection to the Google Sheet, Initialize the workbook/worksheet variables
    sa = gspread.service_account('service_account.json') # Put this into the .env file
    ss = sa.open(WB)
    db = ss.worksheet(DB)
    cd = ss.worksheet(CD)
    cdb = ss.worksheet(CDB)
    logSheet = ss.worksheet('Log')

    # # Pull and Parse the API Data
    # ssl._create_default_https_context = ssl._create_unverified_context
    # url = URL_LINK
    # req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    # response = urlopen(req)
    # data_json = json.loads(response.read())
    # members = data_json['member_list']
    # ssData = []

    # # Add the necessary data from each member to the 2D-array to paste into the spreadsheet
    # newMember = []
    # for m in members:
    #     newMember.append(myDate+'-'+m['username'])
    #     newMember.append(myDate)
    #     newMember.append(m['username'])
    #     newMember.append(m['fame'])
    #     newMember.append(m['levels']['house']['level'])
    #     newMember.append(m['levels']['character']['level'])
    #     newMember.append(m['levels']['fishing']['level'])
    #     newMember.append(m['levels']['woodcutting']['level'])
    #     newMember.append(m['levels']['mining']['level'])
    #     newMember.append(m['levels']['stonecutting']['level'])
    #     newMember.append(m['levels']['crafting']['level'])
    #     newMember.append(m['levels']['carving']['level'])
    #     newMember.append(m['battle']['kills']['value'])
    #     newMember.append(m['battle']['deaths']['value'])
    #     newMember.append(m['harvests']['harvests']['value'])
    #     newMember.append(m['profession']['crafts']['value'])
    #     newMember.append(m['profession']['carves']['value'])
    #     newMember.append(m['misc']['event_actions']['value'])
    #     newMember.append(m['misc']['fatigue_actions']['value'])
    #     newMember.append(m['misc']['total_actions']['value'])
    #     newMember.append(m['misc']['experience_gained']['value'])
    #     newMember.append(m['misc']['gold_looted']['value'])
    #     newMember.append(round(m['harvests']['resources']['value']))
    #     newMember.append(m['misc']['total_event_score']['value'])
    #     newMember.append(m['misc']['strongest_monster_killed']['id'])
    #     newMember.append(m['stats']['base']['value'])
    #     newMember.append(m['training']['base_damage']['trains'])
    #     newMember.append(m['training']['base_armor']['trains'])
    #     newMember.append(m['training']['multistrike_chance']['trains'])
    #     newMember.append(m['training']['critical_hit_chance']['trains'])
    #     newMember.append(m['training']['critical_hit_damage']['trains'])
    #     newMember.append(m['training']['toughness']['trains'])
    #     newMember.append(m['training']['counter_attack_damage']['trains'])
    #     newMember.append(m['training']['healing_boost']['trains'])
    #     newMember.append(m['training']['fishing_boost']['trains'])
    #     newMember.append(m['training']['woodcutting_boost']['trains'])
    #     newMember.append(m['training']['mining_boost']['trains'])
    #     newMember.append(m['training']['stonecutting_boost']['trains'])
    #     newMember.append(m['training']['crafting_boost']['trains'])
    #     newMember.append(m['training']['carving_boost']['trains'])
    #     tempCry = m['clan_donations'].get('crystals')
    #     tempPlat = m['clan_donations'].get('platinum')
    #     if tempCry:
    #         newMember.append(m['clan_donations']['crystals'])
    #     else:
    #         newMember.append(0)
    #     if tempPlat:
    #         newMember.append(m['clan_donations']['platinum'])
    #     else:
    #         newMember.append(0)

    #     ssData.append(newMember)
    #     newMember=[]

    # # now take the top 10 clans public data and log it
    # url2 = "https://avabur.com/api/clans/"
    # req2 = Request(url2, headers={'User-Agent': 'XYZ/3.0'})
    # response2 = urlopen(req2)
    # data_json2 = json.loads(response2.read())
    # clan_data = []

    # for d in data_json2[:9]:
    #     temp_data = []
    #     temp_data.append(myDate+"-"+str(d['id']))
    #     temp_data.append(myDate)
    #     temp_data.append(d['id'])
    #     temp_data.append(d['name'])
    #     temp_data.append(d['level'])
    #     temp_data.append(d['level_percent'])
    #     temp_data.append(d['experience'])
    #     temp_data.append(d['total_experience'])
    #     temp_data.append(d['level_cost'])
    #     temp_data.append(d['buildings'])
    #     temp_data.append(d['maxbuildings'])
    #     temp_data.append(d['godlevel'])
    #     temp_data.append(d['members'])
    #     temp_data.append(d['maxmembers'])
    #     temp_data.append(d['exptax'])
    #     temp_data.append(d['goldtax'])
    #     temp_data.append(d['restax'])
    #     temp_data.append(d['droptax'])
    #     clan_data.append(temp_data)

    # # Take the parsed clan data and append it to the clan_database spreadsheet
    # cdb.append_rows(clan_data)

    # # Take the parsed data and append it to the database spreadsheet
    # db.append_rows(ssData)

    # Take the date/time and append it the bottom of the logSheet
    logSheet.append_row([myDateTime])

    # # Update the current day's data
    # cd.delete_rows(2,31)
    # cd.append_rows(ssData)

if __name__ == '__main__':
    main()