import cv2
img = cv2.imread("solar-system.jpg")



cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (255,255,255)
            )
cv2.putText(img,
            "Mercury",
            (130,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Venus",
            (200,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Earth",
            (260,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Mars",
            (320,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Jupiter",
            (440,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Saturn",
            (660,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Uranus",
            (890,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (255,255,255)
            )
cv2.putText(img,
            "Neptune",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.9,
            (255,255,255)
            )

cv2.imshow("output",img)
cv2.waitKey(0)