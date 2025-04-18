from django.core.management.base import BaseCommand
from knowledge_base.models import Topic, Lesson

class Command(BaseCommand):
    help = 'Popula o banco com dados iniciais de hacking'

    def handle(self, *args, **options):
        # 1. Cria tópicos
        sql_topic = Topic.objects.create(
            name="SQL Injection",
            description="Ataques em bancos de dados SQL",
            icon="fa-database"
        )

        xss_topic = Topic.objects.create(
            name="XSS",
            description="Cross-Site Scripting",
            icon="fa-code"
        )

        # 2. Cria lições
        Lesson.objects.create(
            title="SQLi Básico",
            content="Como explorar vulnerabilidades SQL...",
            topic=sql_topic,
            code_example="SELECT * FROM users WHERE id = 1 OR 1=1 --"
        )

        Lesson.objects.create(
            title="XSS Refletido",
            content="Ataque XSS que executa scripts maliciosos...",
            topic=xss_topic,
            code_example="<script>alert('XSS');</script>"
        )

        # 3. Mensagem de sucesso
        self.stdout.write(
            self.style.SUCCESS('✅ Banco populado com 2 tópicos e 2 lições!')
        )