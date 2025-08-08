from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='empresa')
    icono = models.ImageField(upload_to='empresa')
    imagen_base = models.ImageField(upload_to='empresa')
    mostrar_icon = models.BooleanField(default=True)
    mostrar_lang = models.BooleanField(default=False)
    limite_pedidos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='tiendas')
    mostrar_foto = models.BooleanField(default=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.empresa.nombre} - {self.direccion}"

class Landing(models.Model):
    LAYOUT_CHOICES = [
        ('contained', 'Contained'),
        ('full_width', 'Full width'),
    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='landings')
    nombre = models.CharField(max_length=50, default='home')
    layout_mode = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default='contained')

    def __str__(self):
        return self.nombre

SECTION_CHOICES = [
    ('section_topbar_offers', 'Topbar Offers'),
    ('section_hero', 'Hero'),
    ('section_category', 'Category Showcase'),
    ('section_banners', 'Banners'),
    ('section_how_we_work', 'How We Work'),
    ('section_gallery', 'Gallery'),
    ('section_about_us', 'About Us'),
    ('section_testimonials', 'Testimonials'),
    ('section_features', 'Features'),
    ('section_cta_section', 'CTA'),
    ('section_newsletter', 'Newsletter'),
    ('section_map', 'Map'),
    ('section_clients', 'Clients'),
    ('footer', 'Footer'),
]

class Section(models.Model):
    landing = models.ForeignKey(Landing, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=50, choices=SECTION_CHOICES)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    variant = models.CharField(max_length=50, blank=True)
    bg_color = models.CharField(max_length=7, blank=True)
    text_color = models.CharField(max_length=7, blank=True)
    link_color = models.CharField(max_length=7, blank=True)
    accent_color = models.CharField(max_length=7, blank=True)
    button_bg_color = models.CharField(max_length=7, blank=True)
    button_text_color = models.CharField(max_length=7, blank=True)
    card_bg_color = models.CharField(max_length=7, blank=True)
    card_text_color = models.CharField(max_length=7, blank=True)
    padding_y = models.CharField(max_length=20, blank=True)
    padding_x = models.CharField(max_length=20, blank=True)
    container_max_width = models.CharField(max_length=20, blank=True)
    css_id = models.CharField(max_length=50, blank=True)
    css_class = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.landing.nombre} - {self.name}"

class LandingContent(models.Model):
    landing = models.OneToOneField(Landing, on_delete=models.CASCADE, related_name='content')
    topbar_enabled = models.BooleanField(default=False)
    topbar_rotation_ms = models.IntegerField(default=0)
    hero_title = models.CharField(max_length=200, blank=True)
    hero_description = models.TextField(blank=True)
    hero_button_label = models.CharField(max_length=100, blank=True)
    hero_button_url = models.URLField(blank=True)

    def __str__(self):
        return f"Contenido {self.landing.nombre}"

class TopbarOffer(models.Model):
    content = models.ForeignKey(LandingContent, on_delete=models.CASCADE, related_name='offers')
    text = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
