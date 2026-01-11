import streamlit as st
import pandas as pd

class DataService:
    @staticmethod
    def init_data():
        """Initialize session state data if not present."""
        if 'class_data' not in st.session_state:
            data = {
                'Nama': ['Budi Santoso', 'Siti Aminah', 'Reza Pratama', 'Ayu Lestari', 'Doni Kurniawan', 'Fani Rahma', 'Gilang Saputra', 'Hana Pertiwi'],
                'Level': [5, 4, 2, 6, 1, 3, 4, 5],
                'XP': [520, 410, 150, 680, 50, 320, 400, 550],
                'Kelancaran_Avg': [85, 78, 45, 92, 30, 65, 70, 88], 
                'Status_Hari_Ini': ['Lancar', 'Lancar', 'Terbata', 'Lancar', 'Terbata', 'Normal', 'Normal', 'Lancar'],
                'Kata_Sulit': [[], ['Menyapu'], ['Meng-gelin-ding', 'Per-pus-ta-ka-an'], [], ['Sa-ya', 'Bo-la'], ['Me-nyan-yi'], ['Ber-mai-nan'], []],
                'Diagnosis': [
                    "Konsisten. Tingkatkan ke buku cerita bergambar.",
                    "Ragu di kata kerja berimbuhan 'Me-'.",
                    "Kesulitan mengeja kata > 3 suku kata.",
                    "Excellent. Siap untuk materi paragraf.",
                    "Masih mengeja huruf per huruf.",
                    "Perlu latihan pernapasan.",
                    "Terburu-buru menabrak tanda baca.",
                    "Intonasi natural."
                ]
            }
            st.session_state.class_data = pd.DataFrame(data)

    @staticmethod
    def get_class_data():
        """Get the class dataframe."""
        if 'class_data' not in st.session_state:
            DataService.init_data()
        return st.session_state.class_data

    @staticmethod
    def get_student_data(student_name):
        """Get specific student data by name."""
        df = DataService.get_class_data()
        return df[df['Nama'] == student_name].iloc[0]

    @staticmethod
    def is_monitoring_active():
        if 'monitoring_active' not in st.session_state:
            st.session_state.monitoring_active = False
        return st.session_state.monitoring_active

    @staticmethod
    def set_monitoring_active(active: bool):
        st.session_state.monitoring_active = active

    @staticmethod
    def simulate_activity():
        """Simulate random student activity updates."""
        import random
        
        if 'class_data' not in st.session_state:
            DataService.init_data()
            
        df = st.session_state.class_data
        
        # Select random students to update (e.g., 2-3 students)
        indices = random.sample(range(len(df)), k=random.randint(2, 4))
        
        for idx in indices:
            # 1. Update XP
            xp_gain = random.randint(10, 50)
            df.at[idx, 'XP'] += xp_gain
            
            # Simple level logic: Level up every 100 XP
            # Adjusting to match approx data: Level = XP // 100 (approx)
            # We won't strictly enforce formula, just increment level if they cross a 100 mark
            old_xp = df.at[idx, 'XP'] - xp_gain
            if (df.at[idx, 'XP'] // 100) > (old_xp // 100):
                 df.at[idx, 'Level'] += 1
            
            # 2. Update Kelancaran Avg (small fluctuation)
            current_avg = df.at[idx, 'Kelancaran_Avg']
            change = random.randint(-5, 5)
            new_avg = max(0, min(100, current_avg + change))
            df.at[idx, 'Kelancaran_Avg'] = new_avg
            
            # 3. Update Status Hari Ini (Weighted random)
            statuses = ['Lancar', 'Normal', 'Terbata']
            weights = [0.6, 0.3, 0.1] # More likely to be Lancar
            new_status = random.choices(statuses, weights=weights, k=1)[0]
            df.at[idx, 'Status_Hari_Ini'] = new_status
            
        st.session_state.class_data = df
