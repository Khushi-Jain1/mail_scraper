## Step 1: Install OS essentials

    sudo apt-get update

    sudo apt-get upgrade

## Step 2: Download source code 

    git clone 

    cd mail_scraper/

## Step 3: Create virtual environment

    pip install virtualenv

    python3 -m venv .email_env

    source .email_venv/bin/activate

    pip install -r requirements.txt

## Step 4: Load Fixtures

<!-- to dump fixture -->

python manage.py dumpdata appname > json_file_path

<!-- to load fixture -->

python manage.py loaddata

## Step 5: Update settings.ini

    Add necessary infomation to mail_scraper/settings.ini

## Step 6: Add cron
