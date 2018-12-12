import textwrap

from django.db import models

from django.conf import settings
from e_logs.core.utils.webutils import StrAsDictMixin
from e_logs.core.utils.loggers import err_logger
from .services.telegram_bot import TelegramBot
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from email.header import Header

import os
import smtplib


class Feedback(StrAsDictMixin, models.Model):
    MESSAGE = textwrap.dedent(
        """
        <b>Пользователь</b>: {usr}
        <b>Почта</b>: {email}
        <b>Цех</b>: {plant}
        <b>Путь</b>: {url}
        <b>Тема</b>: {theme}
        <b>Cообщение</b>:
        {text}
        """
    )

    # MAIL = textwrap.dedent(
    #     """
    #     From: {email}
    #     To: {email}
    #     Subject: "Kazzinc Elog Feedback"

    #     {msg}
    #     """
    # )



    bot = TelegramBot(channel=settings.FEEDBACK_TG_BOT["channel"],
                      token=settings.FEEDBACK_TG_BOT["token"],
                      proxy=settings.FEEDBACK_TG_BOT["proxy"])

    theme = models.CharField(max_length=200, verbose_name='Тема', null=True, blank=True)
    text = models.CharField(max_length=1000, verbose_name='Сообщение', null=True, blank=True)
    plant = models.CharField(max_length=50, verbose_name='Цех', null=True, blank=True)
    url = models.CharField(max_length=256, verbose_name="URL", null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name='Почта', null=True, blank=True)
    filenames = models.TextField(verbose_name="Имена файлов", default="")
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def send_feedback(self):
        msg = Feedback.MESSAGE.format(
            usr=self.username,
            email=self.email,
            plant=self.plant,
            url=self.url,
            theme=self.theme,
            text=self.text,
        )
        # self._send_telegram(msg)
        self._send_mail(msg)




    def _send_telegram(self, msg):
        Feedback.bot.send_message(msg)
        filenames = self.filenames.split(",")
        if filenames[0]:
            files = []
            for filename in filenames:
                dirpath = os.path.join(os.path.dirname(__file__), "media")
                filepath = os.path.join(dirpath, filename)
                files.append(open(filepath, "rb"))
            Feedback.bot.send_media(files)
        return self
    
    def _send_mail(self, msg):
        msg = msg.replace('\n', '<br/>')
        print(msg)
        mail = settings.FEEDBACK_MAIL["mail"]
        password = settings.FEEDBACK_MAIL["password"]
        msg = MIMEText(msg, "html", _charset="UTF-8")
        msg['Subject'] = Header("Kazzinc Elog Feedback", "utf-8")
        # mail_text = Feedback.MAIL.format(
        #     email=mail,
        #     msg=msg
        # )
        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(mail, password)
            server.sendmail(mail, mail, msg.as_string())
            server.close()
        except Exception as e:
            err_logger.critical("Почта накрылась!", e)