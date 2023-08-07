# Sending_Mail_with_Django

## Technology Stack

* Backend
  * Django
* Database
  * SQLite3

## Tech Stack Involved

<div style="display: flex;justify-content: center;">

<img height="64px" width="auto" src="https://image.flaticon.com/icons/svg/919/919852.svg">
<img height="64px" width="auto" src="https://www.w3schools.com/whatis/img_css.jpg">
<img height="64px" width="auto" src="https://www.drupal.org/files/project-images/bootstrap-stack.png">
<img height="64px" width="auto" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png">
<img height="64px" width="auto" src="https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png">

<div/>

<br/>
<br/>


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:samir321-pixel/Sending_Mail_with_Django.git
```

## Install Requirements:

```bash
pip install -r requirements.txt
```

## Apply the migrations:

```bash
python manage.py migrate
```
## Add your GmailID and Password in settings.py
```
EMAIL_HOST_USER = 'yourgmailid.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'
```

## Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **http://127.0.0.1:8000/**.


## Useful Resources

- [Django Docs](https://docs.djangoproject.com/en/3.0/)
- [Django_Mail](https://docs.djangoproject.com/en/3.1/topics/email/)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide)



## Cron setup
To set up a cron job to execute a Django management command once every 24 hours, you can use the system's cron scheduling utility. Here's how you can do it:

1. **Open the Terminal**:
   Open the terminal or command prompt on your server or development environment.

2. **Edit Crontab**:
   Type the following command to edit the crontab file:

   ```
   crontab -e
   ```

3. **Add a New Cron Job**:
   In the crontab file, add a new line to schedule the execution of your Django management command. The syntax for scheduling a cron job is as follows:

   ```
   minute hour day month day_of_week command_to_run
   ```

   To execute the Django management command every day at a specific time (e.g., 2:00 AM), you can use the following syntax:

   ```
   0 2 * * * /path/to/python /path/to/manage.py your_custom_command
   ```

   Replace `/path/to/python` with the path to your Python executable and `/path/to/manage.py` with the path to your Django project's `manage.py` file. Replace `your_custom_command` with the name of your custom management command.

   For example:

   ```
   0 2 * * * /usr/bin/python3 /path/to/your/project/manage.py send_event_emails
   ```

4. **Save and Exit**:
   Save the crontab file and exit the text editor.

5. **Verify the Cron Job**:
   To verify that the cron job has been set up correctly, you can list the current cron jobs using the following command:

   ```
   crontab -l
   ```

   This will display a list of scheduled cron jobs. Make sure your newly added cron job is listed.

The above configuration will run your Django management command every day at 2:00 AM. Adjust the timing as needed to match your desired execution time.

Remember that the paths and commands mentioned above should be adjusted according to your server's environment and project structure. Additionally, consider setting up proper error handling and logging in your custom management command to monitor its execution.



## Windows Cron
In Windows, you can't use the traditional `cron` utility, as it's a UNIX-based utility. However, you can achieve similar scheduling functionality using the built-in Windows Task Scheduler. Here's how you can set up a scheduled task to execute your Django management command:

1. **Open Windows Task Scheduler**:
   Press `Win + R` to open the Run dialog, then type `taskschd.msc` and press Enter. This will open the Task Scheduler.

2. **Create a Basic Task**:
   In the right-hand Actions pane, click on "Create Basic Task." This will open a wizard that guides you through the task creation process.

3. **Name and Description**:
   Give your task a name and description. Click "Next."

4. **Task Trigger**:
   Choose "Daily" for the trigger and click "Next."

5. **Start Date and Time**:
   Set the starting date and time for the task to run. Click "Next."

6. **Action**:
   Choose "Start a Program" as the action and click "Next."

7. **Program/Script**:
   Browse and select the path to your Python executable. For example, it might be `C:\Python39\python.exe`.

8. **Add Arguments (optional)**:
   In the "Add arguments" field, provide the path to your `manage.py` file and the name of your custom command. For example:

   ```
   C:\path\to\your\project\manage.py send_event_emails
   ```

9. **Start in (optional)**:
   In the "Start in" field, provide the directory where your `manage.py` file is located.

10. **Finish**:
    Review your settings and click "Finish" to create the task.

11. **Modify Task** (optional):
    After creating the task, you might want to modify its properties. Right-click on the task in the middle pane and select "Properties." You can adjust settings such as triggering, timing, and advanced settings.

12. **Run Task Manually (optional)**:
    To test the task, right-click on it and select "Run." This will manually trigger the task's execution.

Your Windows Task Scheduler will now execute your Django management command according to the schedule you've set. Please note that the steps might vary slightly depending on your version of Windows, but the general process remains the same.