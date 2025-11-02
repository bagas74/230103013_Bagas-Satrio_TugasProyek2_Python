# tracker/rekap_kelas.py

from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """
    Manajer untuk mengelola data mahasiswa dan penilaian dalam satu kelas.
    """

    def __init__(self):
        """
        Inisialisasi RekapKelas dengan dictionary kosong untuk menyimpan data.
        Struktur: {nim: {'mhs': obj_mahasiswa, 'nilai': obj_penilaian}}
        """
        self.data_mahasiswa = {}

    def tambah_mahasiswa(self, nim, nama):
        """
        Menambahkan mahasiswa baru ke dalam rekap.
        """
        if nim not in self.data_mahasiswa:
            self.data_mahasiswa[nim] = {
                'mhs': Mahasiswa(nim, nama),
                'nilai': Penilaian(nim)
            }
            print(f"Mahasiswa {nama} (NIM: {nim}) berhasil ditambahkan.")
        else:
            print(f"Error: Mahasiswa dengan NIM {nim} sudah ada.")

    def set_hadir(self, nim, persen):
        """
        Mengatur persentase kehadiran untuk mahasiswa berdasarkan NIM.
        """
        if nim in self.data_mahasiswa:
            self.data_mahasiswa[nim]['mhs'].hadir_persen = persen
            print(f"Kehadiran {self.data_mahasiswa[nim]['mhs'].nama} diatur ke {persen}%.")
        else:
            print(f"Error: NIM {nim} tidak ditemukan.")

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        """
        Mengatur semua nilai untuk mahasiswa berdasarkan NIM.
        """
        if nim in self.data_mahasiswa:
            nilai_obj = self.data_mahasiswa[nim]['nilai']
            nilai_obj.quiz = quiz
            nilai_obj.tugas = tugas
            nilai_obj.uts = uts
            nilai_obj.uas = uas
            print(f"Nilai untuk {self.data_mahasiswa[nim]['mhs'].nama} berhasil diatur.")
        else:
            print(f"Error: NIM {nim} tidak ditemukan.")

    def predikat(self, nilai_akhir):
        """
        Menentukan predikat huruf (A-E) berdasarkan nilai akhir.
        Menggunakan skala yang disimpulkan dari contoh output.
        """
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >= 75:
            return "B"
        elif nilai_akhir >= 60:
            return "C"
        elif nilai_akhir >= 50:
            return "D"
        else:
            return "E"

    def rekap(self):
        """
        Menghasilkan daftar dictionary yang berisi rekap data semua mahasiswa.
        """
        records = []
        for nim, data in self.data_mahasiswa.items():
            mhs_obj = data['mhs']
            nilai_obj = data['nilai']
            
            nilai_akhir_mhs = nilai_obj.nilai_akhir()
            predikat_mhs = self.predikat(nilai_akhir_mhs)
            
            records.append({
                "nim": mhs_obj.nim,
                "nama": mhs_obj.nama,
                "hadir": mhs_obj.hadir_persen,
                "nilai_akhir": nilai_akhir_mhs,
                "predikat": predikat_mhs
            })
        return records