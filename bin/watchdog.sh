#!/bin/bash
# --- Cúpula de Persistencia SVR-1 ---

while true; do
  # 1. Verificar si Tor está vivo
  if ! pgrep -x "tor" > /dev/null; then
    tor -f ~/Bunker_SVR/seguridad/torrc &
    echo "[!] Tor reiniciado" >> ~/Bunker_SVR/logs/sistema.log
  fi

  # 2. Verificar si el Motor Principal está vivo
  if ! pgrep -f "main.py" > /dev/null; then
    python ~/Bunker_SVR/main.py &
    echo "[!] Motor SVR-1 relanzado" >> ~/Bunker_SVR/logs/sistema.log
  fi

  sleep 60
done
