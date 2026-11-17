"""Q4: Building Long Text – Repeated += vs str.join() vs io.StringIO."""
import time
import io

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    # TODO 1 Completed: Build the same text using a single str.join() call
    return ";".join(parts) + ";" if parts else ""

def build_stringio(parts):
    buf = io.StringIO()
    for p in parts:
        buf.write(p)
        buf.write(";")
    return buf.getvalue()

if __name__ == "__main__":
    t0 = time.perf_counter(); a = build_plus(items); t_plus = time.perf_counter() - t0
    t0 = time.perf_counter(); b = build_join(items); t_join = time.perf_counter() - t0
    t0 = time.perf_counter(); c = build_stringio(items); t_sio = time.perf_counter() - t0
    print("same text:", a == b == c, "| length:", len(b))
    print(f"+= time: {t_plus:.4f} s   join time: {t_join:.4f} s   StringIO time: {t_sio:.4f} s")
