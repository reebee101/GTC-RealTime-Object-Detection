<p align="center">
  <b>bdd100k-object-detection</b><br>
  🚗🚌 Real-time Object Detection for Autonomous Vehicles on BDD100K • 🔎📷 → 🤖
</p>

# BDD100K — Object Detection with YOLOv8 🎯

**Goal:** train and evaluate a YOLOv8 model on the BDD100K dataset for autonomous driving scenarios.  
**Highlights:** ✅ Data preparation ✅ Model training (30, 50, 100 epochs) ✅ Evaluation ✅ Confusion matrices ✅ Real-world predictions


---

## 🧭 Project overview

- **Dataset:** [BDD100K](https://www.kaggle.com/datasets/marquis03/bdd100k)  
- **Classes:** car, bus, truck, person, traffic light, traffic sign, bike, motor, train, other
- **Model:** YOLOv8

---

## ✅ What we did

### Phase 1 — Data Preparation & Feature Engineering 📂
- Downloaded dataset (Kaggle: `marquis03/bdd100k`)  
- Converted annotations to YOLO format  
- Split into train/val/test sets
- Visualized data

### Phase 2 — Model Training ⚡
- **Epochs tested:** 30, 50, 100 

### Phase 3 — Evaluation 📊
- **Training curves:** box_loss, cls_loss, dfl_loss steadily decreased  
- **Metrics:**  
  - mAP@50 improved from ~0.45 (30 epochs) → ~0.56 (100 epochs)  
  - mAP@50-95 reached ~0.28 → ~0.38  
  - Precision stabilized around 0.65–0.70  
  - Recall improved from ~0.35 → ~0.53  

- **Confusion matrices:**  
  - Showed strong car detection, moderate for trucks & buses, weaker for small objects like pedestrians, bicycles, and traffic signs  

### Phase 4 — Predictions 🚀
- Tested on street images & dashcam frames  
- Successfully detected cars (high confidence), traffic signs, and lights  

---

## 📌 Key Learnings
- More epochs (100) significantly improved recall and mAP  
- Background class dominates — needs balancing  
- Small objects (traffic signs/lights) remain challenging  
- Real-world predictions confirm the model generalizes well  

---

**Developed as part of our GTC ML internship ✨**
