import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_user, smtp_pass, recipients, subject, body):
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass
        self.recipients = recipients
        self.subject = subject
        self.body = body

    def send_email(self, attachment_path):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject

        msg.attach(MIMEText(self.body, 'plain'))

        try:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                               f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(part)
        except FileNotFoundError:
            logging.error(f"Fichier joint introuvable : {attachment_path}")
            return

        try:
            # Paramètres SMTP pour Gmail
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # Port pour TLS

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Démarrer TLS
            server.login(self.smtp_user, self.smtp_pass)
            server.send_message(msg)
            server.quit()  # Utiliser server.quit() pour fermer la connexion
            logging.info(f"Email envoyé avec succès à {', '.join(self.recipients)}!")
        except Exception as e:
            logging.error(f"Erreur lors de l'envoi de l'email : {e}")

if __name__ == "__main__":
    recipients = ["beaelie1228@gmail.com", "armelmbia08@gmail.com"]  # liste des emails

    # Sujet de l'email
    subject = "🚀 GitHub Actions a terminé avec succès !"

    # Corps du message (texte dynamique)
    body = """
    hi groupe 1 ! 👋

    Je suis ravi de vous informer que GitHub Actions a bien effectué toutes les étapes du pipeline avec succès ! 🎉

    Voici ce qui a été accompli :
    - 📂 Préprocessing des données terminé.
    - 🤖 Entraînement du modèle effectué.
    - 📊 Évaluation du modèle réalisée.
    - 📦 Archivage du modèle et des résultats.

    Vous pouvez accéder à l'application directement ici : 🌐 https://huggingface.co/spaces/armelmbia/CC_git_hub_group_1

    Le modèle et le rapport d'évaluation sont joints à cet email. 📎

    Bonne journée et à bientôt ! 😊

    Cordialement,
    Votre assistant GitHub Actions 🤖
    """

    # Configuration de l'expéditeur
    sender = EmailSender(
        smtp_user="beaelie1228@gmail.com",  # Votre email
        smtp_pass="cnbe ushg jajh fmdb",  # Votre mot de passe
        recipients=recipients,
        subject=subject,
        body=body
    )

    # Envoi de l'email avec la pièce jointe
    sender.send_email("output.zip")
