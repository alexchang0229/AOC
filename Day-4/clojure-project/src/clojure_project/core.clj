(ns clojure-project.core)
(require '[clojure.string :as str])
(require '[clojure.set])

(defn exp [x n]
  (reduce * (repeat n x)))

(defn calc-points [num-matches]
  (if (= num-matches 0)
    0
    (exp 2 (- num-matches 1))))

(defn process-cards [s]
  (let [numbers (mapv #(Integer/parseInt %) (re-seq #"\d+" s))
        winning-cards (subvec numbers 1 11)
        hand-cards (subvec numbers 11)
        common-elements (clojure.set/intersection (set winning-cards) (set hand-cards))
        matches  (count common-elements)]
        ;; points (calc-points matches)
    matches))



(let [input (slurp "C:/Users/al031880/Desktop/code/AOC/Day-4/input.txt")
      rows (str/split input #"\r")
      matches (map process-cards rows)]
      ;; total-points (reduce + points)
  (def matches (vec matches)))

(defn ones-array [n]
  (vec (repeat n 1)))

;; loop through matches and print
(defn print-matches [matches]
  (loop [i 10]
    (if (>= i 0)
      (do
        (println (str "Card " i ": " (matches i)))
        (recur (dec i)))
      (println "Done."))))

(defn foo
  []
  (print-matches matches))
(foo)



;; (def card-map (hash-map))

;; sum-card-children (map-indexed get-children-cards matches)

;; (defn get-children-cards [index value]
;;   ;; loop through all the children recursively and add their values
;;   (let [card-children (subvec matches index (+ index value))]
;;     card-children))
