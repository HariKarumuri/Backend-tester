# PopularPg_Backend3.0

## following this url for aws hosting 
https://medium.com/code-with-muh/deploy-django-application-on-ec2-with-postgresql-s3-domain-and-ssl-setup-e21143317223


To access an Amazon EC2 instance using SSH and a `.pem` key file, follow these steps:

1. **Locate the `.pem` key file:**

   Open the directory where you have downloaded the `.pem` key file (e.g., `popularpg2.0.pem`). Make sure you have the necessary permissions to access it.

2. **Open a terminal or command prompt:**

   Open a *GITBASH* on your local machine.

3. **Connect to the EC2 instance using SSH:**

   Use the SSH command to connect to the EC2 instance. In the terminal, run the following command:

   ```shell
   ssh -i "popularpg2.0.pem" ubuntu@ec2-13-53-149-253.eu-north-1.compute.amazonaws.com
   ```

   Replace `"popularpg2.0.pem"` with the path to your `.pem` key file, and `ec2-13-53-149-253.eu-north-1.compute.amazonaws.com` with the public DNS or IP address of your EC2 instance.

4. **Provide necessary permissions to the key file:**

   If required, change the permissions of the `.pem` key file using the following command:

   ```shell
   chmod 400 popularpg2.0.pem
   ```

   This step ensures that only the owner of the file has read and write permissions.

5. **Change to the desired directory:**

   Once you have successfully connected to the EC2 instance, navigate to the desired directory using the `cd` command. For example, if your project is located in the `/home/ubuntu/PopularPg_Backend3.0` directory, run:

   ```shell
   cd /home/ubuntu/PopularPg_Backend3.0
   ```

   Adjust the directory path based on the specific location of your project.

## now to start django server for editing and restarting 


