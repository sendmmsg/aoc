;;; machine.el --- description -*- lexical-binding: t; -*-
;;
;; Copyright (C) 2020 Pontus Sköldström
;;
;; Author: Pontus Sköldström <http://github/eponsko>
;; Maintainer: Pontus Sköldström <pontus.skoldstrom@ericsson.com>
;; Created: december 06, 2020
;; Modified: december 06, 2020
;; Version: 0.0.1
;; Keywords:
;; Homepage: https://github.com/eponsko/machine
;; Package-Requires: ((emacs 27.1) (cl-lib "0.5"))
;;
;; This file is not part of GNU Emacs.
;;
;;; Commentary:
;;
;;  description
;;
;;; Code:

(setq machine-stack '())

(defun machine-pop ()
    (interactive)
    (-last-item machine-stack)
    (setq ret  (car machine-stack))
    (setq machine-stack (cdr machine-stack))
    ret
  )

(defun machine-push (arg)
  (interactive)
  (push arg machine-stack)
    )

(defun machine-print-stack ()
  (interactive)
  (message "%s" machine-stack)
  )

(defun machine-execute (instructions)
  (while instructions
    (setq code (-last-item instructions))
    (message "s" code)
    (setq instructions (instructions))
    )
 )

(machine-push 123)
(machine-print-stack)
(machine-pop)

(setq code '((const 2) (const 3) (const 0) (mul) (add)))
(machine-execute code)


(provide 'machine)
;;; machine.el ends here


(defun day61 ()
  (interactive)
  (find-file "/home/eponsko/code/aoc/2020/day6/input")
  (goto-char (point-min))
  (while (re-search-forward "\\(^\\s-*$\\)\n" nil t)
    (replace-match ";")
    (forward-char 1)
    )
  (goto-char (point-min))
  (while (re-search-forward "\n" nil t)
    (replace-match "")
    (forward-char 1)
    )
  (goto-char (point-min))
  (setq unique-chars '())
  (while (char-after)
    (setq charset '())
    (while (and (not (eq (char-after) 'nil)) (not (string= (string (char-after)) ";")) )
      (push (format "%c" (char-after)) charset)
      (forward-char)
      )
    (delete-dups charset)
    (push (length charset) unique-chars)
    (if (char-after) (forward-char))
    )
  (message "Answers per group %s" unique-chars)
  (message "Total value %s" (apply '+ unique-chars))
)
