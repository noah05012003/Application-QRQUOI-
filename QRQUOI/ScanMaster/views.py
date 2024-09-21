from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QRCode, Utilisateur, HistoriqueScan  # Ajoutez les autres modèles utilisés
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
from django.core.files import File
from django.utils import timezone  # Assurez-vous d'importer timezone

@login_required
def index(request):
    context = {'Qrcodes': HistoriqueScan.objects.filter(utilisateur_historique=request.user)}  # Assurez-vous de filtrer par utilisateur connecté si nécessaire
    return render(request, "ScanMaster/HistoriqueA.html", context)

@login_required
def generate_qrcode(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if not url:
            return HttpResponse("Please provide a URL", status=400)

        qr = qrcode.make(url)
        qr_io = BytesIO()
        qr.save(qr_io, format="PNG")
        qr_io.seek(0)  # Important pour remettre le pointeur au début du fichier
        qr_filename = f"qr_{request.user.id}_{timezone.now().strftime('%Y%m%d%H%M%S')}.png"
        qr_code = QRCode.objects.create(
            utilisateur_qrcode=request.user,
            lien=url,
            image=File(qr_io, name=qr_filename)
        )
        return redirect('historique_qrcodes')
    else:
        return render(request, 'ScanMaster/QRgenerator.html')

@login_required
def historique_qrcodes(request):
    qrcodes = QRCode.objects.filter(utilisateur_qrcode=request.user)
    return render(request, 'ScanMaster/HistoriqueP.html', {'qrcodes': qrcodes})