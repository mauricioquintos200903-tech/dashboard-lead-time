#!/usr/bin/env python3
"""
Servidor Dashboard - Lee datos del BI
"""

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

class DashboardHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def main():
    print("=" * 70)
    print("  DASHBOARD LEAD TIME - DATOS DEL BI")
    print("=" * 70)
    
    if not os.path.exists('dashboard_final_bi.html'):
        print("\n❌ No se encontró dashboard_final_bi.html")
        sys.exit(1)
    
    if not os.path.exists('DATOS_DEL_BI.xlsx'):
        print("\n❌ No se encontró DATOS_DEL_BI.xlsx")
        print("\nAsegúrate de tener ambos archivos en la misma carpeta")
        sys.exit(1)
    
    PORT = 8000
    httpd = HTTPServer(('', PORT), DashboardHandler)
    
    print(f"\n✅ Archivos encontrados:")
    print(f"   - dashboard_final_bi.html")
    print(f"   - DATOS_DEL_BI.xlsx")
    
    print(f"\n🚀 Servidor iniciado en Puerto {PORT}")
    print(f"🌐 Abre: http://localhost:{PORT}/dashboard_final_bi.html")
    
    print("\n📌 Características:")
    print("   ✅ Muestra EXACTAMENTE los datos de tu BI")
    print("   ✅ Botón 'ACTUALIZAR' para recargar datos")
    print("   ✅ Filtros interactivos")
    print("   ✅ Gráficos dinámicos")
    
    print("\n💡 Para actualizar:")
    print("   1. Actualiza tu BI en Power BI Desktop")
    print("   2. Exporta datos del BI a Excel")
    print("   3. Reemplaza DATOS_DEL_BI.xlsx")
    print("   4. Click en 'ACTUALIZAR' en el dashboard")
    
    print("\n📌 Presiona CTRL+C para detener\n")
    
    # Abrir automáticamente
    webbrowser.open(f'http://localhost:{PORT}/dashboard_final_bi.html')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✋ Servidor detenido")
        sys.exit(0)

if __name__ == '__main__':
    main()
