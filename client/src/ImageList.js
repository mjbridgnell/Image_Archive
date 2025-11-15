import React, { useState, useEffect } from "react";
import { Display_title } from "./Utils";
import "./Styles.css";

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
          <div id="container" key={i}>
            <button onClick={() => {
              alert('you clicked');
            }}>
              <p>{image}</p>
              <img className="img" src={`/images/${image}`} />
            </button>
          </div>
        ))
      )}
    </div>
  );
}
