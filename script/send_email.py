import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

class EmailSender:
    def __init__(self, smtp_user, smtp_pass, recipients, subject, body):
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass
        self.recipients = recipients
        self.subject = subject
        self.body = body

    def send_email(self, attachment_path):
        # Création du message
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = ", ".join(self.recipients)
        msg['Subject'] = self.subject

        # Corps du message
        msg.attach(MIMEText(self.body, 'html'))

        # Ajout de la pièce jointe
        if os.path.exists(attachment_path):
            part = MIMEBase('application', 'octet-stream')
            with open(attachment_path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(attachment_path)}'
            )
            msg.attach(part)

        # Envoi de l'email
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.smtp_user, self.smtp_pass)
                smtp.sendmail(self.smtp_user, self.recipients, msg.as_string())
            print("✅ Email envoyé avec succès !")
        except Exception as e:
            print(f"❌ Erreur lors de l'envoi de l'email : {e}")

if __name__ == "__main__":
    # Liste des destinataires
    recipients = ["beaelie1228@gmail.com", "armelmbia08@gmail.com"]

    # Sujet de l'email
    subject = "🚀 GitHub Actions a terminé avec succès !"

    # Corps du message (en HTML pour inclure des emojis et des liens)
    body = """
    <html>
      <body>
        <p>Salut le groupe 1 👋</p>
        <p>Je suis ravi de vous informer que <strong>GitHub Actions</strong> a bien effectué toutes les étapes du pipeline avec succès ! 🎉</p>
        <p>Voici ce qui a été accompli :</p>
        <ul>
          <li>📂 Préprocessing des données terminé.</li>
          <li>🤖 Entraînement du modèle effectué.</li>
          <li>📊 Évaluation du modèle réalisée.</li>
          <li>📦 Archivage du modèle et des résultats.</li>
        </ul>
        <p>Vous pouvez accéder à l'application directement ici : <a href="https://huggingface.co/spaces/armelmbia/CC_git_hub_group_1">🌐 Lien de l'application</a>.</p>
        <p>Le modèle et le rapport d'évaluation sont joints à cet email. 📎</p>
        <p>Bonne journée et à bientôt ! 😊</p>
        <p>Cordialement,<br>Votre assistant GitHub Actions 🤖</p>
      </body>
    </html>
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
