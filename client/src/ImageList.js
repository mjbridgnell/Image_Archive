import React, { useState, useEffect } from "react";
import { Display_title } from './Utils';

export function Display_Images() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    fetch("/images")
      .then((res) => res.json())
      .then((data) => {
        setImages(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <Display_title />
      {images.length === 0 ? (
        <p>Loading...</p>
      ) : (
        images.map((image, i) => (
          <div key={i}>
            <img
              src={`/images/${image}`}
              alt={image}
              style={{ width: "200px", margin: "10px" }}
            />
            <p>{image}</p>
          </div>
        ))
      )}
    </div>
  );
}
