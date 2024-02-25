import sys
from pytube import YouTube

def on_complete(stream, file_path):
    print(f"\nDownload completato con successo. File salvato come: {file_path}")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"Download in corso: {percentage_of_completion:.2f}%", end='\r')

def download_video(url, file_name):
    print("Inizializzazione del download...")
    try:
        yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
        
        print(f"Titolo del video: {yt.title}")
        print(f"Dimensione del video: {yt.streams.filter(progressive=True, file_extension='mp4').first().filesize / 1024 / 1024:.2f} MB")
        
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
        if not file_name.endswith('.mp4'):
            file_name += '.mp4'
        
        print("Inizio del download...")
        stream.download(output_path='.', filename=file_name)
        
        print(f"\nDownload completato con successo: {file_name}")
    except Exception as e:
        print(f"Errore durante il download del video: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: script.py <URL del video> <Nome del file>")
    else:
        url = sys.argv[1]
        file_name = sys.argv[2]
        print("Avvio dello script di download da YouTube...")
        download_video(url, file_name)
        print("Script terminato.")

