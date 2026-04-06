import cv2
import numpy as np

def calculate_metrics(img):
    # Menghitung metrik evaluasi kualitas citra
    std_dev = np.std(img)
    hist, _ = np.histogram(img.flatten(), bins=256, range=(0, 256))
    prob = hist / np.sum(hist)
    prob = prob[prob > 0]
    entropy = -np.sum(prob * np.log2(prob))
    dynamic_range = np.max(img) - np.min(img)
    mean_brightness = np.mean(img)
    return {
        'std_dev': std_dev,
        'entropy': entropy,
        'dynamic_range': dynamic_range,
        'mean_brightness': mean_brightness,
    }

def evaluate_enhancement(original, enhanced):
    metrics_orig = calculate_metrics(original)
    metrics_enh = calculate_metrics(enhanced)
    print("Metrik Perbandingan:")
    print("-" * 80)
    print(f"{'Metric':20}{'Original':15}{'Enhanced':15}{'Change':10}")
    print("-" * 80)
    for key in metrics_orig.keys():
        orig_val = metrics_orig[key]
        enh_val = metrics_enh[key]
        change = ((enh_val - orig_val) / orig_val) * 100 if orig_val != 0 else float('inf')
        print(f"{key:20}{orig_val:15.2f}{enh_val:15.2f}{change:+10.2f}%")
    return metrics_orig, metrics_enh


if __name__ == '__main__':
    img = cv2.imread('low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image 'low_contrast.jpg' not found.")
    img_enhanced = cv2.equalizeHist(img)
    cv2.imwrite('enhanced.jpg', img_enhanced)
    print("Hasil enhanced disimpan sebagai 'enhanced.jpg'")
    evaluate_enhancement(img, img_enhanced)
