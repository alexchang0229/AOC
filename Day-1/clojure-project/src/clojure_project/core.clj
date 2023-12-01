(ns clojure-project.core)
(require '[clojure.string])

(defn resolve-char-to-num [s]
  (let [s_1 (clojure.string/replace s #"one" "o1e")
       s_2 (clojure.string/replace s_1 #"two" "t2o")
        s_3 (clojure.string/replace s_2 #"three" "t3e")
        s_4 (clojure.string/replace s_3 #"four" "f4r")
        s_5 (clojure.string/replace s_4 #"five" "f5e")
        s_6 (clojure.string/replace s_5 #"six" "s6e")
        s_7 (clojure.string/replace s_6 #"seven" "s7n")
        s_8 (clojure.string/replace s_7 #"eight" "e8t")
        s_9 (clojure.string/replace s_8 #"nine" "n9n")
        s_0 (clojure.string/replace s_9 #"zero" "z0o")]
       s_0))

(defn find-numbers [s]
  (let [numeric-chars (filter #(Character/isDigit %) (seq s))
        first-num (first numeric-chars)
        last-num (last numeric-chars)]
    (if (> (count numeric-chars) 1)
      (Integer. (str first-num last-num))
      (Integer. (str first-num first-num)))
    ))

(let [file-contents   (slurp "C:/Users/al031880/Desktop/code/AOC/Day-1/data.txt")                                                                                                                                 
      strings (clojure.string/split file-contents #"\n")
      names-to-nums (map resolve-char-to-num strings)
      row-numbers (map find-numbers names-to-nums)
      sum-all (reduce + row-numbers)]
  (def data sum-all))


(defn foo [] (println data))


(foo)